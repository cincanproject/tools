import time
import threading
import sys
import requests
import argparse

class PdfexaminerSendfile:
    def __init__(self):
        self.__report = ""

    def get_report(self):
        self.__report = self.__report.text.strip()
        return self.__report

    def set_report(self, report):
        self.__report = report


    # Progress bar
    @staticmethod
    def progress_bar(stop_thread):
        t2 = threading.currentThread()
        x = 0
        loading = [" Loadin`"," Loadiñ "," Loadìn "," Loaðin "," Loâdin "," Lõadin", " £oadin ", "~Loadin", " Loadin~"]
        while getattr(t2, "run", True):
            time.sleep(0.05)
            if x < len(loading)-1:
                x = x + 1
            else:
                x = 0
            print (loading[x], end="\r")


    # Parse passed arguments
    @staticmethod
    def parse_arguments():
        parser = argparse.ArgumentParser(description='PDFExaminer')
        parser.add_argument('-i', '--input', required=True, help="")
        parser.add_argument('-f', '--format', required=False, help="json, xml, ioc, php, severity, rating, is_malware, text")
        return parser.parse_args()


    # Send file
    def send_file(self, input, datatype):
        url = 'https://www.pdfexaminer.com/pdfapi.php'
        files = {'sample[]': open(input, 'rb')}

        # Post request
        r = requests.post(url, files=files, data=datatype)
        self.set_report(r)



# Main
def main():
    pdfx = PdfexaminerSendfile()
    args = pdfx.parse_arguments()

    # Use JSON format if not defined
    if not args.format:
        datatype =  {'type':'json'}
    elif args.format in "json, xml, ioc, php, severity, rating, is_malware, text":
        datatype = {'type':args.format}
    else:
        print("Unidentified format")
        sys.exit()

    t1 = threading.Thread(target=pdfx.send_file, args=(args.input,datatype,))
    t2 = threading.Thread(target=pdfx.progress_bar, args=("run",))
    t1.start()
    t2.start()
    t1.join()

    # Print out report
    print(pdfx.get_report())

    # Stop progress bar when send_file finishes
    if not t1.isAlive():
        t2.run = False


if __name__ == '__main__':
    main()
