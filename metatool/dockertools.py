import argparse
import os

import docker, docker.errors
import logging
import tarfile
import io
import sys
import re
import pathlib
import json
import datetime
import tempfile
from typing import List, Set, Dict, Tuple, Optional, Any

from metatool import registry
from metatool.commands import ToolCommand, ToolCommands


class ToolImage:
    """A tool wrapped to docker image"""

    def __init__(self, name: str, path: Optional[str] = None, image: Optional[str] = None, pull: bool = False):
        self.logger = logging.getLogger(path)
        self.client = docker.from_env()
        self.name = name
        if path is not None:
            self.image, log = self.client.images.build(path=path)
            self.context = path
            self.__log_dict_values(log)
        elif image is not None:
            if pull:
                # pull first
                self.__get_image(image, pull=True)
            else:
                # just get the image
                try:
                    self.__get_image(image, pull=False)
                except docker.errors.ImageNotFound:
                    # image not found, try to pull it
                    self.__get_image(image, pull=True)
            self.context = '.'  # not really correct, but will do
        else:
            raise Exception("No file nor image specified")
        self.metadata_file = '.METADATA/files.json'
        self.upload_files = {}  # files to upload, key = name in host, value = name in image
        self.file_content = {}  # in-memory content for some flies, key = name in host (but no file there)
        self.upload_tar = None  # tar file to upload
        self.upload_path = "/tmp/upload_files"
        self.download_files = {}  # files to download, key = name in host, value = name in image
        self.download_path = "/tmp/download_files"
        self.unpack_download_files = False
        self.dump_upload_tar = False
        self.output_tar = None
        self.file_pattern = re.compile("\\^(.+)")

    def get_tags(self) -> List[str]:
        return self.image.tags

    def get_creation_time(self) -> datetime.datetime:
        return registry.parse_json_time(self.image.attrs['Created'])

    def __get_image(self, image: str, pull: bool = False):
        """Get Docker image, possibly pulling it first"""
        if pull:
            self.client.images.pull(image)
        self.image = self.client.images.get(image)

    def __process_arg(self, name: str) -> str:
        """Process an argument, detect if a to upload and change to point to the file inside the container"""
        m = self.file_pattern.search(name)
        f_name = name
        if m is not None:
            b_name = m.group(1)
            download = b_name.startswith('^')
            if not download:
                # upload the file
                use_absolute = ".." in b_name  # use absolute paths, if /../ used (ok, quite weak)
                path = pathlib.Path(b_name)
                if use_absolute:
                    f_name = (pathlib.Path(self.upload_path) / path.resolve()).as_posix()
                else:
                    f_name = (pathlib.Path(self.upload_path) / path).as_posix()
                f_name = f_name.replace(':', '_')
                self.upload_files[b_name] = f_name
                self.logger.debug("arg ^%s -> %s", b_name, f_name)
            else:
                # download the file
                b_name = b_name[1:]
                if ".." in b_name or pathlib.Path(b_name).is_absolute():
                    raise Exception("Output paths must be relative to current directory")
                f_name = self.download_path + '/' + b_name
                self.download_files[b_name] = f_name
                self.logger.debug("arg ^^%s -> %s", b_name, f_name)
        return f_name

    def __process_args(self, args: List[str]) -> List[str]:
        """Process list of arguments"""
        return list(map(lambda a: self.__process_arg(a), args))

    def __create_upload_tar(self) -> Optional[bytes]:
        """Copy uploaded files into tar archive"""
        if self.upload_tar:
            # upload tar just given, return it
            with open(self.upload_tar, "rb") as f:
                return f.read()
        if not self.upload_files:
            return None
        file_out = io.BytesIO()
        tar = tarfile.open(mode="w", fileobj=file_out)
        for name, full_t in self.upload_files.items():
            t = pathlib.Path(full_t).relative_to(self.upload_path).as_posix()
            self.logger.debug("upload file %s -> %s", name, t)
            if name in self.file_content:
                # file contents in memory
                data = self.file_content[name].encode('ascii')
                tarinfo = tarfile.TarInfo(name=t)
                tarinfo.size = len(data)
                tar.addfile(tarinfo=tarinfo, fileobj=io.BytesIO(data))
            else:
                # go and pick file from file system
                tar.add(name, arcname=t)
        tar.close()
        return file_out.getvalue()

    def __create_container(self):
        # override entry point to just keep the container running
        container = self.client.containers.create(self.image, entrypoint="sh", stdin_open=True, tty=True)
        container.start()

        # make sure up/download directories exist
        container.exec_run(["mkdir", "-p", self.upload_path])
        container.exec_run(["mkdir", "-p", self.download_path])

        tarball = self.__create_upload_tar()
        if tarball:
            self.logger.debug("Tarball to upload, size %d", len(tarball))
            if self.dump_upload_tar:
                with open("upload_files.tar", "wb") as f:
                    f.write(tarball)
            container.put_archive(path='/tmp/upload_files/', data=tarball)
        return container

    def __container_exec(self, container, cmd_args: List[str]) -> (str, str, int):
        # create the full command line and run with exec
        entry_point = self.image.attrs['Config'].get('Entrypoint')
        if not entry_point:
            entry_point = []
        cmd = self.image.attrs['Config'].get('Cmd')
        if not cmd:
            cmd = []  # 'None' value observed
        full_cmd = entry_point + (cmd_args if cmd_args else cmd)
        exit_code, cmd_output = container.exec_run(full_cmd, demux=True)
        stdout = cmd_output[0] if cmd_output[0] else b''
        stderr = cmd_output[1] if cmd_output[1] else b''
        return stdout, stderr, exit_code

    def __copy_downloaded_files(self, container, stdout: bytes, summary: Optional[Dict]):
        """Copy downloaded files into tar archive"""
        if not self.download_files and not stdout:
            return
        chunks, stat = container.get_archive(self.download_path)

        # FIXME: We read into temporary file, as do not know how to read chunks as tar-file
        tmp_tar = tempfile.NamedTemporaryFile(delete=False)
        for c in chunks:
            tmp_tar.write(c)
        tmp_tar.close()
        read_tar = tarfile.open(tmp_tar.name)

        write_tar = None
        if self.output_tar:
            # Put all output into tar-file
            write_tar = tarfile.open(self.output_tar, "w")
            self.logger.info("Output to %s", self.output_tar)
            out_sum = io.BytesIO(json.dumps(summary, indent=4).encode('ascii'))
            out_file = tarfile.TarInfo(self.metadata_file)
            out_file.size = len(out_sum.getvalue())
            self.logger.debug(" %s", out_file.name)
            write_tar.addfile(out_file, fileobj=out_sum)

        if write_tar and stdout:
            out_file = tarfile.TarInfo('stdout')
            out_file.size = len(stdout)
            self.logger.debug(" %s", out_file.name)
            write_tar.addfile(out_file, fileobj=io.BytesIO(stdout))

        name_re = re.compile("^" + pathlib.Path(self.download_path).name + "/?")
        for m in read_tar.getmembers():
            n_name = name_re.sub('', m.name)
            if n_name == "":
                continue
            self.logger.debug(" %s", n_name)
            content = read_tar.extractfile(m)
            if write_tar:
                m.name = n_name
                write_tar.addfile(m, fileobj=content)
            else:
                with open(n_name, "wb") as f:
                    f.write(content)
        read_tar.close()
        write_tar.close() if write_tar else None
        os.unlink(tmp_tar.name)
        return

    def __write_file_metadata(self, command: ToolCommand, args: List[str]) -> Dict[str, Any]:
        files_v = []
        for name in [str(k) for k in self.download_files.keys()] if self.download_files else ['stdout']:
            f = {'name': name}
            if command.out_type:
                f['type'] = command.out_type
            files_v.append(f)
        cmd_v = {
            'tool': self.name,
            'args': ' '.join(args),
        }
        in_files = []
        for f in self.upload_files.keys():
            if f not in self.file_content:
                f = {'name': f}
                if command.in_type:
                    f['type'] = command.in_type
                in_files.append(f)
        history_v = {
            'input': in_files,
            'command': cmd_v,
        }
        return {
            'files': files_v,
            'history': history_v,
        }

    def __run(self, command: ToolCommand) -> (str, str, int):
        """Run native tool in container with given arguments"""
        cmd_args = self.__process_args(command.args)
        self.logger.debug("args: %s", ' '.join(cmd_args))

        container = self.__create_container()
        stdout, stderr, exit_code = self.__container_exec(container, cmd_args)
        container.kill()

        if exit_code == 0:
            # write stdout, copy files to filesystem if any
            self.__copy_downloaded_files(container, b'', None)
        return stdout, stderr, exit_code

    def run(self, args: List[str]) -> (str, str, int):
        """Run native tool in container, return output"""
        return self.__run(ToolCommand(args))

    def run_get_string(self, args: List[str]) -> str:
        """Run native tool in container, return output as a string"""
        r = self.__run(ToolCommand(args))
        return r[0].decode('utf8') + r[1].decode('utf8')

    def __log_dict_values(self, log: Set[Dict[str, str]]) -> None:
        """Log values from a dict as debug"""
        for i in log:
            v = i.values()
            self.logger.debug("{}".format(*v).strip())

    def file_to_copy_from_context(self, file: str, prefix: bool = True) -> str:
        """Create path for sample file inside docker context (for unit testing) """
        return ('^' if prefix else '') + str(pathlib.Path(self.context) / file)

    def get_commands(self) -> ToolCommands:
        """Read commands from commands.json from docker image, empty list if none"""
        container = self.client.containers.create(self.image)
        try:
            raw_tar, stat = container.get_archive(path='/cincan/commands.json')
        except docker.errors.APIError:
            return ToolCommands({})
        buffer = io.BytesIO()
        for r in raw_tar:
            buffer.write(r)
        buffer.seek(0)
        tarball = tarfile.open("r", fileobj=buffer)
        commands = {}
        for f in tarball.getmembers():
            c = tarball.extractfile(f).read()
            js = json.loads(c)
            self.logger.debug(json.dumps(js))
            commands = ToolCommands(js)
        container.remove()
        return commands

    def set_file_content(self, content: str) -> str:
        """Set input file content directly"""
        self.file_content['in-str'] = content
        return 'in-str'

    def __do_run(self, command: ToolCommand) -> (str, str, int):
        """Do-run native tool in container with input from tar-file"""
        cmd_args = self.__process_args(command.args)
        self.logger.debug("args: %s", ' '.join(cmd_args))

        container = self.__create_container()
        stdout, stderr, exit_code = self.__container_exec(container, cmd_args)
        container.kill()

        if exit_code == 0:
            # write all output into tar file
            out_sum = self.__write_file_metadata(command, cmd_args)
            self.__copy_downloaded_files(container,
                                         None if self.download_files else stdout,  # use stdout if no other output
                                         out_sum)
        container.remove()
        return stdout, stderr, exit_code

    def do_run(self, in_file: str, args: List[str] = None,
               in_type: Optional[str] = None, out_type: Optional[str] = None) -> (str, str, int):
        """Do -sub command to run the native tool"""
        exp_out_file = None
        if self.output_tar and self.get_commands().get_output_to_file_option():
            exp_out_file = "output"  # use explicit output file supported by the tool
        if self.upload_tar:
            # Input file and type in tar
            self.logger.info("Read input from %s", self.upload_tar)
            with tarfile.open(self.upload_tar, "r") as f:
                js = json.load(f.extractfile(self.metadata_file))
            cmd_line = self.get_commands().parse_command(js, write_output=exp_out_file)
        else:
            # Using command line
            cmd_line = self.get_commands().command_line(in_file, args, in_type, out_type,
                                                        write_output=exp_out_file)
        self.logger.debug(cmd_line)
        return self.__do_run(cmd_line)

    def do_get_string(self, in_file: str, args: List[str] = None,
                      in_type: Optional[str] = None, out_type: Optional[str] = None) -> str:
        """Do -sub command to run the native tool, get output as string"""
        r = self.do_run(in_file, args, in_type, out_type)
        return r[0].decode('utf8') + r[1].decode('utf8')


def tool_with_file(file: str) -> ToolImage:
    path = pathlib.Path(file).parent.name
    return ToolImage(path, path=path)


def image_default_args(sub_parser):
    """Default arguments for sub commands which load docker image"""
    sub_parser.add_argument('tool', help="the tool and possible arguments", nargs=argparse.REMAINDER)
    sub_parser.add_argument('-p', '--path', help='path to Docker context')
    sub_parser.add_argument('-u', '--pull', action='store_true', help='Pull image from registry')
    sub_parser.add_argument('--unpack', action='store_true',
                            help="Unpack output file(s) from tar")
    sub_parser.add_argument('--dump-upload-files', action='store_true',
                            help="Dump the uploaded tar file into 'upload_files.tar'")


def main():
    m_parser = argparse.ArgumentParser()
    m_parser.add_argument("-l", "--log", dest="logLevel", choices=['DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL'],
                          help="Set the logging level", default='INFO')
    subparsers = m_parser.add_subparsers(dest='sub_command')

    run_parser = subparsers.add_parser('run')
    image_default_args(run_parser)

    list_parser = subparsers.add_parser('list')
    list_parser.add_argument('-i', '--in', dest='input', action='store_true', help='Show input formats')
    list_parser.add_argument('-o', '--out', action='store_true', help='Show output formats')
    list_parser.add_argument('-t', '--tags', action='store_true', help='Show tags')

    hint_parser = subparsers.add_parser('hint')
    image_default_args(hint_parser)

    mani_parser = subparsers.add_parser('manifest')
    image_default_args(mani_parser)

    do_parser = subparsers.add_parser('do')
    image_default_args(do_parser)
    do_parser.add_argument('-t', '--in-tar', help='Input as tar-file')
    do_parser.add_argument('-r', '--read-file', help='Input file to read')
    do_parser.add_argument('-s', '--in-str', help='Input string')
    do_parser.add_argument('-i', '--in-format', help='Input format')
    do_parser.add_argument('-o', '--out-format', help='Output format')

    args = m_parser.parse_args()

    logging.basicConfig(format='%(message)s', level=getattr(logging, args.logLevel))
    if args.sub_command in {'run', 'hint', 'do'}:
        if len(args.tool) == 0:
            raise Exception('Missing tool name argument')
        name = args.tool[0]
        if args.path is None:
            tool = ToolImage(name, image=name, pull=args.pull)
        elif args.path is not None:
            tool = ToolImage(name, path=args.path)
        else:
            tool = ToolImage(name)  # should raise exception
        tool.unpack_download_files = args.unpack
        tool.dump_upload_tar = args.dump_upload_files
        all_args = args.tool[1:]
        if args.sub_command == 'run':
            # sub command 'run'
            ret = tool.run(all_args)
            sys.stdout.buffer.write(ret[0])
            sys.stderr.buffer.write(ret[1])
            sys.exit(ret[2])  # exit code
        elif args.sub_command == 'do':
            # sub command 'do'
            tool.output_tar = 'output.tar' if not tool.unpack_download_files else None  # Default is tar-format output!
            read_file = args.read_file
            if args.in_tar:
                tool.upload_tar = args.in_tar
            elif args.in_str is not None:
                read_file = tool.set_file_content(args.in_str)
            elif read_file is None:
                raise Exception('Must specify either --in-tar, --read-file, or --in-str')
            ret = tool.do_run(in_file=read_file, args=all_args, in_type=args.in_format, out_type=args.out_format)
            if tool.get_commands().get_output_to_file_option():
                # content is handled through output file, dump stdout visible as it should not contain the data
                sys.stdout.buffer.write(ret[0])
            sys.stderr.buffer.write(ret[1])
            sys.exit(ret[2])  # exit code
        else:
            # sub command 'hint'
            prefix = "run ".format(name)
            hints = tool.get_commands().command_hints()
            print("# {} {}".format(','.join(tool.get_tags()), registry.format_time(tool.get_creation_time())))
            if len(hints) > 0:
                print(prefix + ("\n" + prefix).format(name).join(hints))
            else:
                print("No command hints")
                sys.exit(1)
    elif args.sub_command == 'manifest':
        # sub command 'manifest'
        if len(args.tool) == 0:
            raise Exception('Missing tool name argument')
        name = args.tool[0]
        reg = registry.ToolRegistry()
        info = reg.fetch_manifest(name)
        print(json.dumps(info, indent=2))
    else:
        format_str = "{0:<25}"
        if args.input:
            format_str += " {2:<30}"
        if args.out:
            format_str += " {3:<30}"
        if args.tags:
            format_str += " {4:<20}"
        format_str += " {1}"
        reg = registry.ToolRegistry()
        tool_list = reg.list_tools()
        for tool in sorted(tool_list):
            lst = tool_list[tool]
            print(format_str.format(lst.name, lst.description, ",".join(lst.input), ",".join(lst.output),
                                    ",".join(lst.tags)))
