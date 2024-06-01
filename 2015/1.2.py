#!/usr/bin/env python3

import sys

FILE: str = sys.argv[1]

def floor_identifier(FILE: str) -> int:
    up: int = 0
    down: int = 0
    floor: int = 0
    with open(FILE) as data:
        line: str = data.readline()
        for position, char in enumerate(line):
            if char == '(':
                up += 1
            elif char == ')':
                down += 1
            floor = up - down
            if floor < 0:
                return position + 1
                break

postion: int =  floor_identifier(FILE)
print(postion)

