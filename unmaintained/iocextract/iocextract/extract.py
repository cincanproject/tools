import iocextract
import os
import time
from datetime import datetime
import argparse


class Extractor:
    def __init__(self):
        pass

    @staticmethod
    def load_file(path):
        """Loads and returns file contents"""
        if not os.path.exists(path):
            print("file", path, "not found!")
            exit(1)
        with open(path, 'r') as reader:
            content = reader.read()
        return content

    @staticmethod
    def write_file(extracted_list, path, delimiter="\n", extension="txt"):
        """Writes a list of extracted strings to path folder in a timestamped
        and delimited file

        Parameters
        ----------
        extracted_list : list
            List of extracted strings
        path : str
            Path to output folder
        delimiter : str
            Delimiter string
        extension : str
            Output file extension
        """
        timestamp = datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d-%H:%M:%S')
        split = os.path.splitext(path)
        if len(split[1].strip()) != 0:
            extension = split[1].strip()
            path = os.path.split(path)[0]
        if extension[0] == ".":
            extension = extension[1:]
        complete_name = "{}.{}".format(timestamp, extension)
        complete_path = os.path.join(path, complete_name)
        with open(complete_path, 'w') as writer:
            for item in extracted_list:
                writer.write("{}{}".format(item, delimiter))

    @staticmethod
    def extract_urls(content_list, strip=False):
        """Extracts all urls from the given list of strings

        Parameters
        ----------
        content_list : list
            A list containing strings to analyze
        strip : bool
            Boolean to determine if possible garbage should be stripped from
            the end of the url

        Returns
        -------
        extracted : list
            List of extracted urls
        """
        extracted = []
        for content in content_list:
            extract = list(iocextract.extract_urls(content, refang=False, strip=strip))
            extracted.extend(extract)
        print(extracted)
        return extracted

    @staticmethod
    def extract_hashes(content_list, types=None):
        """Extracts selected md5, sha1, sha256, sha512 hash types
        from the given list of strings

        Parameters
        ----------
        content_list : list
            A list containing strings to analyze
        types : list
            A list containing strings indicating types of hashes to be
            extracted, None will extract all supported hashes

        Returns
        -------
        extracted : list
            List of extracted hashes
        """

        extracted = []
        for content in content_list:
            if types is None:
                extract = list(iocextract.extract_hashes(content))
                extracted.extend(extract)
            else:
                if 'md5' in types:
                    extract = list(iocextract.extract_md5_hashes(content))
                    extracted.extend(extract)
                if 'sha1' in types:
                    extract = list(iocextract.extract_sha1_hashes(content))
                    extracted.extend(extract)
                if 'sha256' in types:
                    extract = list(iocextract.extract_sha256_hashes(content))
                    extracted.extend(extract)
                if 'sha512' in types:
                    extract = list(iocextract.extract_sha512_hashes(content))
                    extracted.extend(extract)
        return extracted

    @staticmethod
    def extract_emails(content_list):
        """extracts all emails from the given list of strings

        parameters
        ----------
        content_list : list
            a list containing strings to analyze

        returns
        -------
        extracted : list
            list of extracted emails
        """
        extracted = []
        for content in content_list:
            extract = list(iocextract.extract_emails(content, refang=True))
            extracted.extend(extract)
        return extracted

    @staticmethod
    def extract_ips(content_list, ipv4=True, ipv6=False):
        """extracts all ips from the given list of strings

        parameters
        ----------
        content_list : list
            a list containing strings to analyze
        ipv4 : bool
            Should ipv4 be extracted
        ipv6 : bool
            Should ipv6 be extracted
        returns
        -------
        extracted : list
            list of extracted ips
        """
        extracted = []
        for content in content_list:
            if ipv4:
                extract = list(iocextract.extract_ipv4s(content))
                extracted.extend(extract)
            if ipv6:
                extract = list(iocextract.extract_ipv6s(content))
                extracted.extend(extract)
        return extracted

    @staticmethod
    def remove_duplicates(non_unique_list):
        return list(set(non_unique_list))

def main(argv):
    ext = Extractor()
    content_list = []
    if os.path.isdir(argv.path):
        for f in os.listdir(argv.path):
            complete_path = os.path.join(argv.path, f)
            if not os.path.isdir(complete_path):
                content_list.append(ext.load_file(complete_path))
    elif os.path.isfile(argv.path):
        content_list.append(ext.load_file(argv.path))
    if argv.url:
        extracted_urls = ext.extract_urls(content_list)
        extracted_urls = Extractor.remove_duplicates(extracted_urls)
        if argv.verbose:
            print("Urls:")
            print(extracted_urls)
        try:
            os.makedirs(os.path.join(argv.output, 'urls'))
        except FileExistsError:
            pass
        if len(extracted_urls) != 0:
            ext.write_file(extracted_urls, os.path.join(argv.output, 'urls'), delimiter="\n")
    if argv.hash:
        extracted_hashes = ext.extract_hashes(content_list)
        extracted_hashes = Extractor.remove_duplicates(extracted_hashes)
        if argv.verbose:
            print("Hashes:")
            print(extracted_hashes)
        try:
            os.makedirs(os.path.join(argv.output, 'hashes'))
        except FileExistsError:
            pass
        if len(extracted_hashes) != 0:
            ext.write_file(extracted_hashes, os.path.join(argv.output, 'hashes'), delimiter="\n")
    if argv.ip:
        extracted_ips = ext.extract_ips(content_list, ipv4=True, ipv6=True)
        extracted_ips = Extractor.remove_duplicates(extracted_ips)
        if argv.verbose:
            print("Ips:")
            print(extracted_ips)
        try:
            os.makedirs(os.path.join(argv.output, 'ips'))
        except FileExistsError:
            pass
        if len(extracted_ips) != 0:
            ext.write_file(extracted_ips, os.path.join(argv.output, 'ips'), delimiter="\n")
    if argv.email:
        extracted_emails = ext.extract_emails(content_list)
        extracted_emails = Extractor.remove_duplicates(extracted_emails)
        if argv.verbose:
            print("Emails:")
            print(extracted_emails)
        try:
            os.makedirs(os.path.join(argv.output, 'emails'))
        except FileExistsError:
            pass
        if len(extracted_emails) != 0:
            ext.write_file(extracted_emails, os.path.join(argv.output, 'emails'), delimiter="\n")


if __name__ == '__main__':
    argparser = argparse.ArgumentParser(
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    argparser.add_argument("-u", "--url",
                           action='store_true',
                           help="Sets url extraction on.")
    argparser.add_argument("-e", "--email",
                           action='store_true',
                           help="Sets email extraction on.")
    argparser.add_argument("-i", "--ip",
                           action='store_true',
                           help="Sets ip extraction on.")
    argparser.add_argument("--hash",
                           action='store_true',
                           help="Sets hash extraction on.")
    argparser.add_argument("-v", "--verbose",
                           action='store_true',
                           help="Sets verbosity to high.")

    argparser.add_argument("--output", "-o",
                           required=False,
                           type=str,
                           default="./",
                           help="Output directory.")

    argparser.add_argument("--path", "-p",
                           required=True,
                           type=str,
                           default=None,
                           help="Path to files (directory) or file to check.")

    args = argparser.parse_args()
    main(argv=args)

