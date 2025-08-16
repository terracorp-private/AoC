#!/usr/bin/env python3

import sys
import re
from typing import List

input_file: str = sys.argv[1]

def make_nice(line) -> bool:
    pattern: List = ["ab", "cd", "pq", "xy"]
    for substring in pattern:
        res = re.findall(substring, line)
        if len(res) != 0:
            return False
    return True


def vowel(line) -> bool:
    pattern: str = r'[aeiou]'
    res: list[str] = re.findall(pattern, line)
    if len(res) >= 3:
        return True
    else:
        return False


def doubled(line) -> bool:
    pattern: str = r'(.)\1'
    res: list[str] = re.findall(pattern, line)
    if len(res) != 0:
        return True
    else:
        return False

count = 0
with open(input_file) as data:
    lines = data.read().splitlines()
    for line in lines:
        if vowel(line) and doubled(line) and make_nice(line):
            count += 1
    print(count)
