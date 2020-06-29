import os
import hashlib
import argparse
import requests
import json
import time
from datetime import datetime

class VirusTotal:
    """Simple VirusTotal api control"""
    REQUEST_OK = 200
    LIMIT_EXCEEDED = 204
    BAD_REQUEST = 400
    FORBIDDEN = 403

    def __init__(self, config_file=".config.json", api_key=None):
        with open(config_file) as conf:
            config = json.load(conf)
        self.url = config["url"]
        self.sleep_time = config["api_sleep"]
        self.public = config["public"]
        if api_key is None:
            self._set_api_from_file(config["api_key"])
        else:
            self.api_key = api_key
        self.public_timer_start = 0
        self.requests_sent = 0
        self.urls = []
        self.files = []
        self.hashes = []

    def load_files(self, dir_path):
        """Prepares file paths and hashes for requests

        Parameters
        ----------
        dir_path : str
            Path to the files to scan
        """
        if not os.path.isdir(dir_path):
            print("Given directory doesn't exist")
            exit(1)
        self.files = []
        self.hashes = []
        for file in os.listdir(dir_path):
            file_path = os.path.join(dir_path, file)
            self.files.append(file_path)
            self.hashes.append(VirusTotal.sha256_hash(file_path))

    def load_hashes(self, path):
        """Loads hashes text file and splits the newline delimited sha256 hashes.
        Alternatively loads all text files from folder

        Parameters
        ----------
        path : str
            newline delimited hashes file or folder containing newline delimited hash files
        """
        self.hashes = []
        if os.path.isdir(path):
            for file in os.listdir(path):
                file_path = os.path.join(path, file)
                with open(file_path, 'r') as reader:
                    hashes = reader.read().splitlines()
                for hash in hashes:
                    self.hashes.append(hash)
        elif os.path.isfile(path):
            with open(path, 'r') as reader:
                hashes = reader.read().splitlines()
            for hash in hashes:
                self.hashes.append(hash)
        else:
            print("Given hash file/folder doesn't exist")
            exit(1)

    def load_urls(self, path):
        """Loads url file or folder with multiple files and split the newline delimited urls 
        in the file/files

        Parameters
        ----------
        path : str
            newline delimited urls file or folder containing url files
        """
        self.urls = []
        self.files = []
        if os.path.isdir(path):
            for file in os.listdir(path):
                file_path = os.path.join(path, file)
                with open(file_path, 'r') as reader:
                    urls = reader.read().splitlines()
                for url in urls:
                    self.urls.append(url)
        elif os.path.isfile(path):
            with open(path, 'r') as reader:
                urls = reader.read().splitlines()
            for url in urls:
                self.urls.append(url)
        else:
            print("Given url file/folder doesn't exist")
            exit(1)

    def send_files(self):
        """Sends files to be analyzed, load_files must be called before"""
        for file in self.files:
            if isinstance(file, str):
                with open(file, 'rb') as reader:
                    data = {"file": reader}
                result = requests.post(self.url, data=self.api_key, files=data)
                print("VirusTotal: File: {} Status: {}.".format(
                    file, result.status_code))
                self._check_status(result)

    def _check_status(self, result):
        """Checks if request succeeded and prints error

        Parameters
        ----------
        result : requests.Response

        Returns
        -------
        success : bool
            True if code is 200, else False
        """

        if result.status_code == self.REQUEST_OK:
            print("REQUEST OK")
            return True
        elif result.status_code == self.LIMIT_EXCEEDED:
            print("LIMIT EXCEEDED: API Request limit exceeded.")
        elif result.status_code == self.BAD_REQUEST:
            print("BAD REQUEST: Incorrect api request.")
        elif result.status_code == self.FORBIDDEN:
            print("FORBIDDEN: You don't have enough priviliges")
        else:
            print("UNKNOWN ERROR: {}".format(result))
        return False

    def wait_for_access(self):
        """Waits configured time before returning False if 4 requests have
            been sent"""
        if self.public_timer_start + self.sleep_time > time.time():
            print("Waiting for access... ({} seconds remaining.)".format(
                int(self.public_timer_start + self.sleep_time - time.time())))
            return True
        elif self.requests_sent >= 4:
            self.requests_sent = 0
            return False

    def retrieve_file_reports(self, files_path=None, hashes_file=None):
        """Retrieves file reports using sha256 hash, load_files must be
            called before or files_path should be filled

        Parameters
        ----------
        files_path : str, optional
            loads files optionally inplace
        hashes_path : str, optional
            loads newline delimited hash file inplace

        Returns
        -------
        results : dict
            Dictionary containing report results
        """
        if files_path is not None:
            self.load_files(files_path)
        results = {}
        for index, hash in enumerate(self.hashes):
            res = None
            while res is None or res.status_code == VirusTotal.LIMIT_EXCEEDED:
                while self.public and self.wait_for_access():
                    time.sleep(10)
                url = self.url + "file/report"
                params = {"apikey": self.api_key,
                          "resource": hash,
                          "allinfo": True}
                res = requests.post(url, data=params)
                self.requests_sent += 1
                if self._check_status(res):
                    result = json.loads(res.text)
                    if len(self.files) != 0:
                        results.update({self.files[index]: result})
                    else:
                        results.update({hash: result})
                if self.requests_sent == 4:
                    self.public_timer_start = time.time()
        return results

    def _set_api_from_file(self, api_file):
        """Sets api key from file"""
        try:
            if os.stat(api_file).st_size == 0:
                print("Empty api key file")
                exit(1)
        except FileNotFoundError:
            print("Empty api key file")
            exit(1)
        with open(api_file) as api:
            self.api_key = api.read().strip()


    @staticmethod
    def sha256_hash(file_path):
        """Sha256 Hashes a file"""
        with open(file_path, 'rb') as file:
            sha256 = hashlib.sha256()
            while True:
                data = file.read(8192)
                if not data:
                    break
                sha256.update(data)
            return sha256.hexdigest()

    def retrieve_url_reports(self, url_file=None, scan_if_not_found=False):
        """Retrieves existing reports and optionally scans urls which are
        not in the database, load_urls must be called before or
        url_file must be filled

        Parameters
        ----------
        url_file : str, optional
            newline delimited urls file, if load_urls should be called inplace
        scan_if_not_found : bool, optional
            Determines if urls should be scanned if they are not in the database

        Returns
        -------
        results : dict
            Dictionary containing reports from the requests for each url
        """
        if url_file is not None:
            self.load_urls(url_file)
        results = {}
        for url in self.urls:
            res = None
            while res is None or res.status_code == VirusTotal.LIMIT_EXCEEDED:
                while self.public and self.wait_for_access():
                    time.sleep(10)
                address = self.url + "url/report"
                params = {"apikey": self.api_key,
                          "resource": url,
                          "allinfo": True,
                          "scan": int(scan_if_not_found)}
                res = requests.post(address, data=params)
                self.requests_sent += 1
                if self._check_status(res):
                    result = json.loads(res.text)
                    results.update({url: result})
                if self.requests_sent == 4:
                    self.public_timer_start = time.time()
        return results


def log_results(results, output):
    """Writes simplistic results to given timestamped output file and dumps json to
     .json file"""

    def _delimiter(w):
        w.write("==================================================="
                "==================================================="
                "===================================================\n")
    if not os.path.isdir(os.path.split(output)[0]):
        print("Given output directory d:oesn't exist.")
        exit(1)

    completed_results = {}
    incomplete_results = {}
    invalid = {}
    for key, value in results.items():
        if "positives" in results[key].keys():
            completed_results[key] = results[key]
        elif "permalink" in results[key].keys():
            incomplete_results[key] = results[key]
        else:
            invalid[key] = results[key]
    sorted_keys = sorted(completed_results,
                         key=lambda x: (completed_results[x]['positives']))
    timestamp = datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d-%H:%M:%S')
    split = os.path.splitext(output)
    simple_log = "{}_{}.log".format(split[0], timestamp, split[1])
    with open(simple_log, "w") as writer:
        _delimiter(writer)
        for key in sorted_keys:
            writer.write("Complete results:\n")
            _delimiter(writer)
            writer.write("Scanned: {}\n".format(key))
            writer.write("Link to analysis: {}\n".format(
                results[key]["permalink"]))
            writer.write("Positives/Total: ({}/{})\n".format(
                results[key]["positives"], results[key]["total"]))
        _delimiter(writer)
        if incomplete_results:
            writer.write("Incomplete results:\n")
            _delimiter(writer)
            for key in incomplete_results:
                writer.write("Scanned: {}\n".format(key))
                writer.write("Link to analysis: {}\n".format(
                    results[key]["permalink"]))
                _delimiter(writer)
        if invalid:
            writer.write("Invalid results:\n")
            _delimiter(writer)
            for key in invalid:
                writer.write("Scanned: {}\n".format(key))
                writer.write("Error msg: {}\n".format(
                    results[key]["verbose_msg"]))
                _delimiter(writer)

    json_log = "{}_{}.json".format(os.path.splitext(output)[0], timestamp)
    with open(json_log, 'w') as writer:
        json.dump(results, writer)


def main(argv):
    vt = VirusTotal(argv.config, argv.api_key)
    if args.files is not None:
        vt.load_files(argv.files)
        file_results = vt.retrieve_file_reports()
        if argv.verbose:
            print(json.dumps(file_results, indent=2, sort_keys=True))
        log_results(file_results, os.path.join(argv.output, "file_results"))
        if argv.send:
            vt.send_files()
    if args.files_hash is not None:
        vt.load_hashes(argv.files_hash)
        file_results = vt.retrieve_file_reports()
        if argv.verbose:
            print(json.dumps(file_results, indent=2, sort_keys=True))
        log_results(file_results, os.path.join(argv.output, "hash_results"))
    if args.url_file is not None:
        vt.load_urls(argv.url_file)
        url_results = vt.retrieve_url_reports(scan_if_not_found=argv.send)
        if argv.verbose:
            print(json.dumps(url_results, indent=2, sort_keys=True))
        log_results(url_results, os.path.join(argv.output, "url_results"))


if __name__ == '__main__':
    argparser = argparse.ArgumentParser(
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    argparser.add_argument("-v", "--verbose",
                           action='store_true',
                           help="Sets verbosity to high.")

    argparser.add_argument("--send", "-s",
                           action='store_true',
                           help="Send files/urls to check if reports not "
                                "found.")

    argparser.add_argument("--output", "-o",
                           required=True,
                           type=str,
                           default=None,
                           help="Output directory.")

    argparser.add_argument("--config", "-c",
                           required=False,
                           type=str,
                           default="./config.json",
                           help="Config file path.")

    argparser.add_argument("--api_key", "-a",
                           required=False,
                           type=str,
                           default=None,
                           help="Virustotal API key or file containing the key if not defined falls back to config file"
                                "to find the key file.")

    argparser.add_argument("--files", "-f",
                           required=False,
                           type=str,
                           default=None,
                           help="Path to files to check.")

    argparser.add_argument("--files_hash", "-fh",
                           required=False,
                           type=str,
                           default=None,
                           help="Path to txt file containing file hashes to check.")

    argparser.add_argument("--url_file", "-u",
                           required=False,
                           type=str,
                           default=None,
                           help="File containing newline delimited urls.")

    args = argparser.parse_args()
    if not args.files and not args.url_file and not args.files_hash:
        print("Files directory, hash text file or url text file argument required.")
        exit(1)
    main(argv=args)
