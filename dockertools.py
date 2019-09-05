import argparse
import docker
import docker.errors
import logging
import tarfile
import io
import sys
import re
import pathlib
import json
from typing import List, Set, Dict, Tuple, Optional, Any

from metatool import registry


class ToolImage:
    """A tool wrapped to docker image"""

    def __init__(self, path: Optional[str] = None, image: Optional[str] = None, pull: bool = False):
        self.logger = logging.getLogger(path)
        self.client = docker.from_env()
        if path is not None:
            self.image, log = self.client.images.build(path=path)
            self.context = path
            self.do_log(log)
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
        self.mapped_files = {}  # files to upload, key = name in host, value = name in image
        self.file_content = {}  # in-memory content for some flies, key = name in host (but no file there)
        self.dump_upload_tar = False
        self.file_pattern = re.compile("\\^(.+)")

    def __get_image(self, image, pull: bool = False):
        if pull:
            self.client.images.pull(image)
        self.image = self.client.images.get(image)

    def __process_arg(self, name: str) -> str:
        m = self.file_pattern.search(name)
        f_name = name
        if m is not None:
            b_name = m.group(1)
            f_name = "/tmp/work_files" + (b_name if b_name.startswith('/') else '/' + b_name).replace(':', '_')
            self.mapped_files[b_name] = f_name
            self.logger.info("copy: %s -> %s", b_name, f_name)
        return f_name

    def __process_args(self, args: List[str]) -> List[str]:
        return list(map(lambda a: self.__process_arg(a), args))

    def __copy_extracted_files(self) -> bytes:
        file_out = io.BytesIO()
        tar = tarfile.open(mode="w", fileobj=file_out)
        for name, t in self.mapped_files.items():
            self.logger.debug("in-file %s", name)
            if name in self.file_content:
                # file contents in memory
                data = self.file_content[name].encode('ascii')
                tarinfo = tarfile.TarInfo(name=t[1:])  # strip first '/'
                tarinfo.size = len(data)
                tar.addfile(tarinfo=tarinfo, fileobj=io.BytesIO(data))
            else:
                # go and pick file from file system
                tar.add(name, arcname=t[1:])  # strip first '/'
        tar.close()
        return file_out.getvalue()

    def run(self, args: List[str]) -> bytes:
        cmd_args = self.__process_args(args)
        self.logger.info("args: %s", ' '.join(cmd_args))
        container = self.client.containers.create(self.image, command=cmd_args)
        tarball = self.__copy_extracted_files()
        if self.mapped_files:
            self.logger.debug("Tarball to upload, size %d", len(tarball))
            if self.dump_upload_tar:
                with open("upload_files.tar", "wb") as f:
                    f.write(tarball)
            container.put_archive(path='/', data=tarball)
        container.start()
        container.wait()
        logs = container.attach(logs=True)
        container.remove()
        return logs

    def run_get_string(self, args: List[str]):
        return self.run(args).decode('ascii')

    def do_log(self, log: Set[Dict[str, str]]) -> None:
        for i in log:
            v = i.values()
            self.logger.debug("{}".format(*v).strip())

    def file_to_copy(self, file : str) -> str:
        return '^' + str(pathlib.Path(self.context) / file)

    def get_commands(self) -> List[Dict[str, Any]]:
        container = self.client.containers.create(self.image)
        raw_tar, stat = container.get_archive(path='/cincan/commands.json')
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
            commands = js['commands']
        container.remove()
        return commands

    def list_command_line(self) -> List[str]:
        commands = self.get_commands()
        lines = []
        for c in commands:
            c_str = " ".join(c['command'])
            lines.append(c_str.replace("<file>", "^<file>"))
        return lines

    def do_run(self, args: List[str], in_file: str, in_type: Optional[str], out_type: Optional[str]) -> bytes:
        all_commands = self.get_commands()
        match_commands = []
        for c in all_commands:
            if '<file>' not in c['command']:
                continue
            if in_type is not None and in_type != c.get('input'):
                continue
            if out_type is not None and out_type != c.get('output'):
                continue
            match_commands.append(c)
        if len(match_commands) != 1:
            raise Exception("Single command should match given input/output filter, now:\n{}".format(
                "\n".join(map(lambda x: "{}{}".format(" -i {}".format(x['input']) if 'input' in x else "",
                                                      " -o {}".format(x['output']) if 'output' in x else ""),
                              match_commands))))
        command = match_commands[0]['command']
        true_args = []
        for arg in command:
            if arg == "<file>":
                true_args.append("^{}".format(in_file))
            else:
                true_args.append(arg)
        for arg in args:
            true_args.append(arg)
        self.logger.info(" ".join(true_args))
        return self.run(true_args)


def image_default_args(sub_parser):
    sub_parser.add_argument('tool', help="the tool and possible arguments", nargs=argparse.REMAINDER)
    sub_parser.add_argument('-p', '--path', help='path to Docker context')
    sub_parser.add_argument('-u', '--pull', action='store_true', help='Pull image from registry')
    sub_parser.add_argument('--dump-upload-files', action='store_true',
                            help="Dump the uploaded tar file into 'upload_files.tar'")


def main():
    m_parser = argparse.ArgumentParser()
    m_parser.add_argument("-l", "--log", dest="logLevel", choices=['DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL'],
                          help="Set the logging level")
    subparsers = m_parser.add_subparsers(dest='sub_command')

    run_parser = subparsers.add_parser('run')
    image_default_args(run_parser)

    subparsers.add_parser('list')

    hint_parser = subparsers.add_parser('hint')
    image_default_args(hint_parser)

    do_parser = subparsers.add_parser('do')
    image_default_args(do_parser)
    do_parser.add_argument('-r', '--read-file', help='Input file to read')
    do_parser.add_argument('-s', '--in-str', help='Input string')
    do_parser.add_argument('-i', '--in-format', help='Input format')
    do_parser.add_argument('-o', '--out-format', help='Output format')

    args = m_parser.parse_args()
    if args.logLevel:
        logging.basicConfig(level=getattr(logging, args.logLevel))
    if args.sub_command in {'run', 'hint', 'do'}:
        if len(args.tool) == 0:
            raise Exception('Missing tool name argument')
        name = args.tool[0]
        if args.path is None:
            tool = ToolImage(image=name, pull=args.pull)
        elif args.path is not None:
            tool = ToolImage(path=args.path)
        else:
            tool = ToolImage()  # should raise exception
        tool.dump_upload_tar = args.dump_upload_files
        all_args = args.tool[1:]
        if args.sub_command == 'run':
            sys.stdout.buffer.write(tool.run(all_args))
        elif args.sub_command == 'do':
            read_file = args.read_file
            if args.in_str is not None:
                read_file = 'in-str'
                tool.file_content[read_file] = args.in_str
            elif read_file is None:
                raise Exception('Must specify either --read-file or --in-str')
            sys.stdout.buffer.write(tool.do_run(all_args, in_file=read_file,
                                                in_type=args.in_format, out_type=args.out_format))
        else:
            prefix = "run {} ".format(name)
            print(prefix + ("\n" + prefix).format(name).join(tool.list_command_line()))
    else:
        reg = registry.ToolRegistry()
        tool_list = reg.list_tools().values()
        for lst in tool_list:
            print('{0:<30}{1:<40}{2}'.format(lst.name, lst.input, lst.output))


if __name__ == '__main__':
    main()
