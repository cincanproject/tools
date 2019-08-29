import argparse
import docker
import logging
import tarfile
import io
import os
import re
from typing import List, Set, Dict, Tuple, Optional


class ToolImage:
    """A tool wrapped to docker image"""

    def __init__(self, file: Optional[str] = None, image: Optional[str] = None):
        self.logger = logging.getLogger(file)
        self.context = os.path.realpath(file)
        self.temp_dir = os.path.realpath('cincan-temp')
        self.logger.info("context: %s", self.context)
        self.client = docker.from_env()
        if file is not None:
            self.image, log = self.client.images.build(path=file)
            self.do_log(log)
        elif image is not None:
            self.image = self.client.images.get(image)
        else:
            raise Exception("No file nor image specified")
        self.tarball = None
        self.mapped_files = {}
        self.file_pattern = re.compile("\\^(.+)")

    def extract_file_and_copy_if(self, name: str) -> str:
        m = self.file_pattern.search(name)
        f_name = name
        if m is not None:
            b_name = m.group(1)
            f_name = "/tmp/work_files" + (b_name if b_name.startswith('/') else '/' + b_name).replace(':', '_')
            self.mapped_files[b_name] = f_name
            self.logger.info("copy: %s -> %s", b_name, f_name)
        return f_name

    def extract_files_to_copy(self, args: List[str]) -> List[str]:
        return list(map(lambda a: self.extract_file_and_copy_if(a), args))

    def copy_files_to_container(self) -> None:
        file_out = io.BytesIO()
        tar = tarfile.open(mode="w", fileobj=file_out)
        for name, t in self.mapped_files.items():
            self.logger.debug("in-file %s", name)
            tar.add(name, arcname=t[1:])  # strip first '/'
        tar.close()
        self.tarball = file_out.getvalue()
        self.logger.debug("Tarball to upload, size %d", len(self.tarball))
        # with open("files_to_upload.tar", "wb") as f:
        #    f.write(self.tarball)

    def run(self, args: List[str]):
        cmd_args = self.extract_files_to_copy(args)
        self.logger.info("command: %s", ' '.join(cmd_args))
        container = self.client.containers.create(self.image, command=cmd_args)
        self.copy_files_to_container()
        if self.tarball is not None:
            container.put_archive(path='/', data=self.tarball)
        container.start()
        container.wait()
        return container.attach(logs=True)

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
    args = m_parser.parse_args()
    if args.logLevel:
        logging.basicConfig(level=getattr(logging, args.logLevel))
    if args.path is None:
        tool = ToolImage(image=args.tool[0])
    elif args.path is not None:
        tool = ToolImage(file=args.path)
    else:
        tool = ToolImage() # should raise exception
    all_args = args.tool[1:]
    print(tool.run(all_args))


if __name__ == '__main__':
    main()
