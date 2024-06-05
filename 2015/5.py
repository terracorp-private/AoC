#!/usr/bin/env python3

import sys
import re

FILE: str = sys.argv[1]


def parser(line) -> str:
    vowels: str = r'[aeiou]'
    res = re.findall(vowels, line)
    if len(res) >= 3:
        return res


with open(FILE) as data:
    lines = data.readlines()
    vowels = [parser(line) for line in lines if parser(line) is not None]
    print(vowels)
