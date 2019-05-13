#!/usr/bin/env python3

from argparse import ArgumentParser, FileType
import json
import sys
import whois

def whois_query(ip):
    try:
        w = whois.whois(ip)
        print(w)
    except Exception as e:
        json.dumps(e, indent=4)

if __name__ == '__main__':
    usage = "usage: %prog [options] ip"
    parser = ArgumentParser(description="Query IP")

    parser.add_argument("ip", nargs='?', help="ip to query")
    parser.add_argument("-f", '--file', dest="file",
                        help="file to load IPs from", type=FileType('r'))

    args = parser.parse_args()

    if args.file:
        for ip in args.file:
            whois_query(ip.strip())
    else:
        whois_query(args.ip)

