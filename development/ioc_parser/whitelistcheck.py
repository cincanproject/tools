#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys
from pymispwarninglists import WarningLists

if __name__ == '__main__':
    warninglists = WarningLists(slow_search=True)

    ioc_list = set()
    
    for line in sys.stdin:
        line = line.strip().split('\t')
        ioc_list.add(line[-1])
    
    for ioc in ioc_list:
        r = warninglists.search(ioc)
        if r:
            continue
        print(ioc)
