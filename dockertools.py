import argparse
import docker
import logging
import os
from typing import List, Set, Dict, Tuple, Optional


class ToolImage:
    """A tool wrapped to docker image"""

    def __init__(self, file: Optional[str] = None, image: Optional[str] = None):
        self.logger = logging.getLogger(file)
        self.context = os.path.realpath(file)
        self.logger.info("context: %s", self.context)
        self.client = docker.from_env()
        if file is not None:
            self.image, log = self.client.images.build(path=file)
            self.do_log(log)
        elif image is not None:
            self.image = self.client.images.get(image)
        else:
            raise Exception("No file nor image specified")
        # print("{} args={}".format(file, args))

    def run(self, args: List[str]):
        samples_dir = self.context + '/samples'
        return self.client.containers.run(self.image, volumes={samples_dir: {'bind': "/samples"}}, command=args)

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
    print(tool.run(args.args))


if __name__ == '__main__':
    main()
