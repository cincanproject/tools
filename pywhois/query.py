#!/usr/bin/env python3

import whois
import sys

try:
    w = whois.whois(sys.argv[1])
    print(w)
except Exception as e:
    print(e)
