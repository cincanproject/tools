import argparse
import docker
import logging
from typing import List, Set, Dict, Tuple, Optional


class ToolImage:
    """A tool wrapped to docker image"""

    def __init__(self, file: str, args: List[str]):
        self.file = file
        self.args = args
        self.logger = logging.getLogger(file)
        self.client = docker.from_env()
        self.image, log = self.client.images.build(path=file)
        self.do_log(log)
        print("{} args={}".format(file, args))

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
    run_parser.add_argument('-a', '--args', nargs='*')
    args = m_parser.parse_args()
    if args.logLevel:
        logging.basicConfig(level=getattr(logging, args.logLevel))
    tool = ToolImage(args.path, args.args)


if __name__ == '__main__':
    main()
