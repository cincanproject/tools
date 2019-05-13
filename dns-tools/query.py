#!/usr/bin/env python3

from argparse import ArgumentParser, FileType
import json

import gatherdns

def query_dns(domain, nameserver=None, rdtypes=None):
    data = {}

    dnsinfo = gatherdns.GatherDNS(domain, nameserver)
    data['auth_nameserver'] = dnsinfo.find_authoritative_nameserver(domain)

    dnsinfo.query_domain(rdtypes)
    for rdtype in rdtypes: 
        function = getattr(dnsinfo, 'get_{}_record'.format(rdtype))
        result = function()
        if result is not None:
            data[rdtype] = result

    return data

if __name__ == '__main__':
    usage = "usage: %prog [options] domain"
    parser = ArgumentParser(description="Query DNS")

    parser.add_argument("domain", nargs='?', help="domain to query")
    parser.add_argument("-s", "--nameserver", dest="nameserver",
                      help="nameserver to query")

    parser.add_argument("-t", "--rdtypes", dest="rdtypes", default="A,AAAA,NS,MX,SOA,CNAME,TXT,PTR",
                        help="comma separated list of record types", type=str)

    parser.add_argument("-f", '--file', dest="file",
                        help="file to load domains from", type=FileType('r'))

    args = parser.parse_args()

    rdtypes = args.rdtypes.upper().split(',')

    if args.file:
        for domain in args.file.readlines():
            print(json.dumps(query_dns(domain, args.nameserver, rdtypes), indent=4))
    else:
        print(json.dumps(query_dns(args.domain, args.nameserver, rdtypes), indent=4))

