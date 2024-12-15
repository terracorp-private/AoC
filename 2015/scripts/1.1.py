#!/usr/bin/env python3

# The first implementation requires "re", which is not optimal.

import sys
import re

FILE: str = sys.argv[1]

def floor_identifier(FILE) -> int:
    with open(FILE) as data:
        line: str = data.readline()
        up: int = len(re.findall(r'\(',line))
        down: int = len(re.findall(r'\)',line))
        return up-down

floor: int =  floor_identifier(FILE)


# The better way to solve the problem is to use a build in str.count() method.

def floor_identifierV2(FILE) -> int:
    with open(FILE) as data:
        line: str = data.readline()
        up: int = line.count('(')
        down: int = line.count(')')
        return up-down

floor: int =  floor_identifierV2(FILE)
