import argparse
import docker
import docker.errors
import logging
import tarfile
import io
import sys
import re
from typing import List, Set, Dict, Tuple, Optional


class ToolImage:
    """A tool wrapped to docker image"""

    def __init__(self, path: Optional[str] = None, image: Optional[str] = None, pull: bool = False):
        self.logger = logging.getLogger(path)
        self.client = docker.from_env()
        if path is not None:
            self.image, log = self.client.images.build(path=path)
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
        else:
            raise Exception("No file nor image specified")
        self.mapped_files = {}
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
            # with open("files_to_upload.tar", "wb") as f:
            #    f.write(tarball)
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


def main():
    m_parser = argparse.ArgumentParser()
    m_parser.add_argument("-l", "--log", dest="logLevel", choices=['DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL'],
                          help="Set the logging level")
    subparsers = m_parser.add_subparsers(help='sub-command')
    run_parser = subparsers.add_parser('run')
    run_parser.add_argument('tool', help="the tool and possible arguments",  nargs=argparse.REMAINDER)
    run_parser.add_argument('-p', '--path', help='path to Docker context')
    run_parser.add_argument('-u', '--pull', action='store_true', help='Pull image from registry')
    args = m_parser.parse_args()
    if args.logLevel:
        logging.basicConfig(level=getattr(logging, args.logLevel))
    if args.path is None:
        tool = ToolImage(image=args.tool[0], pull=args.pull)
    elif args.path is not None:
        tool = ToolImage(path=args.path)
    else:
        tool = ToolImage()  # should raise exception
    all_args = args.tool[1:]
    sys.stdout.buffer.write(tool.run(all_args))


if __name__ == '__main__':
    main()
