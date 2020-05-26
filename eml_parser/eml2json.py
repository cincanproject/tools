#!/usr/bin/env python3

import argparse
import datetime
import json
import base64
from eml_parser import eml_parser
import os

def json_serial(obj):
    if isinstance(obj, datetime.datetime):
        serial = obj.isoformat()
        return serial

def parse_eml(raw_email):
    parsed_eml = eml_parser.decode_email_b(raw_email, include_raw_body=True, include_attachment_data=True)
    print(json.dumps(parsed_eml, default=json_serial))

def extract_attachments(raw_email, outpath):
    os.makedirs(outpath, exist_ok=True)
    m = eml_parser.decode_email_b(raw_email, include_attachment_data=True)
    if 'attachment' in m:
        for a in m.get('attachment', []):
            filename = a['filename']
            filename = os.path.join(outpath, filename)

            with open(filename, 'wb') as a_out:
                a_out.write(base64.b64decode(a['raw']))

if __name__ == "__main__":
    argparser = argparse.ArgumentParser()
    argparser.add_argument('eml', type=argparse.FileType('rb'), help='EML file to read')
    argparser.add_argument('-e', dest='extract', nargs='?', const=os.getcwd(), help='Extract attachments to path')
    args = argparser.parse_args()
    eml_file = args.eml.read()
    args.eml.close()

    if args.extract:
        extract_attachments(eml_file, args.extract)

    parse_eml(eml_file)
