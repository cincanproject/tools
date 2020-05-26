import time
from tqdm import tqdm
import threading
import sys
import requests
import argparse

# Progress bar
def progress_bar(stop_thread):
    t2 = threading.currentThread()
    with tqdm(total=100, file=sys.stdout) as pbar:
        while getattr(t2, "run", True):
            time.sleep(0.5)
            pbar.update(10)


# Parse passed arguments
def parse_arguments():
    parser = argparse.ArgumentParser(description='PDFExaminer')
    parser.add_argument('-i', '--input', required=True, help="")
    parser.add_argument('-f', '--format', required=False, help="json, xml, ioc, php, severity, rating, is_malware, text")
    return parser.parse_args()


# Send file
def send_file(input, datatype):
    t = threading.currentThread()
    url = 'https://www.pdfexaminer.com/pdfapi.php'
    print("Sending " + input)
    files = {'sample[]': open(input, 'rb')}

    # Post request
    r = requests.post(url, files=files, data=datatype)

    print(r.text.strip())


def main():
    args = parse_arguments()

    # Use JSON format if not defined
    if not args.format:
        datatype =  {'type':'json'}
    elif args.format in "json, xml, ioc, php, severity, rating, is_malware, text":
        datatype = {'type':args.format}
    else:
        print("Unidentified format")
        sys.exit()

    t1 = threading.Thread(target=send_file, args=(args.input,datatype,))
    t2 = threading.Thread(target=progress_bar, args=("run",))
    t1.start()
    t2.start()
    t1.join()

    # Stop progress bar when send_file finishes
    if not t1.isAlive():
        t2.run = False
        t2.join()


if __name__ == '__main__':
    main()


