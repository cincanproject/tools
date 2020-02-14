#!/usr/bin/env python3

import argparse
import datetime
import json
import eml_parser

def json_serial(obj):
    if isinstance(obj, datetime.datetime):
        serial = obj.isoformat()
        return serial

def parse_eml(fhdl):
    raw_email = fhdl.read()
    parsed_eml = eml_parser.eml_parser.decode_email_b(raw_email, include_raw_body=True)
    print(json.dumps(parsed_eml, default=json_serial))
    fhdl.close()

if __name__ == "__main__":
    argparser = argparse.ArgumentParser()
    argparser.add_argument('eml', type=argparse.FileType('rb'), help='EML file to read')
    args = argparser.parse_args()
    parse_eml(args.eml)
