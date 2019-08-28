import argparse
import docker
import logging
import tarfile
import io
import os
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

    def copy_files_to_temp(self, files: List[str]) -> None:
        file_out = io.BytesIO()
        tar = tarfile.open(mode="w", fileobj=file_out)
        for p in files:
            self.logger.debug("in-file %s", p)
            tar.add(p)
        tar.close()
        self.tarball = file_out.getvalue()
        self.logger.debug("Tarball to upload, size %d", len(self.tarball))
        # with open("files_to_upload.tar", "wb") as f:
        #     f.write(self.tarball)

    def run(self, args: List[str]):
        samples_dir = self.context + '/samples'
        container = self.client.containers.create(self.image, volumes={samples_dir: {'bind': "/samples"}}, command=args)
        if self.tarball is not None:
            # container.exec_run(cmd='mkdir -p /tmp/cincan-work')
            container.put_archive(path='/tmp', data=self.tarball)
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
    m_parser.add_argument('-c', '--command')
    m_parser.add_argument("-l", "--log", dest="logLevel", choices=['DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL'],
                          help="Set the logging level")
    subparsers = m_parser.add_subparsers()
    run_parser = subparsers.add_parser('run')
    run_parser.add_argument('-p', '--path')
    run_parser.add_argument('-i', '--image')
    run_parser.add_argument('-s', '--in-string')
    run_parser.add_argument('-f', '--in-file')
    run_parser.add_argument('-a', '--args', nargs='*')
    args = m_parser.parse_args()
    if args.logLevel:
        logging.basicConfig(level=getattr(logging, args.logLevel))
    if args.image is not None:
        tool = ToolImage(image=args.image)
    elif args.path is not None:
        tool = ToolImage(file=args.path)
    else:
        tool = ToolImage() # should raise exception
    if args.in_file is not None:
        tool.copy_files_to_temp([args.in_file])
    print(tool.run(args.args))


if __name__ == '__main__':
    main()
