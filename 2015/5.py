#!/usr/bin/env python3

import sys

FILE: str = sys.argv[1]

with open(FILE) as data:
    line = data.readlines()
    print(line)
