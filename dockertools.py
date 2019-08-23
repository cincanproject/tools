import argparse

def runImage(file, args):
    print("{} args={}".format(file, args))


def main():
    m_parser = argparse.ArgumentParser()
    m_parser.add_argument('-c', '--command')
    subparsers = m_parser.add_subparsers()
    run_parser = subparsers.add_parser('run')
    run_parser.add_argument('-p', '--path')
    run_parser.add_argument('-a', '--args')
    args = m_parser.parse_args()
    print("FIXME docker run -v FIXME {} {}".format(args.path, args.args))

if __name__ == '__main__':
    main()
