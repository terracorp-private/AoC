#!/usr/bin/env python

# In this schematic, two numbers are not part numbers because they are not adjacent to a symbol:
# 114 (top right) and 58 (middle right).
# Every other number is adjacent to a symbol and so is a part number; their sum is 4361.
# Of course, the actual engine schematic is much larger. What is the sum of all of the
# part numbers in the engine schematic?


import re
import numpy as np

file: str = '/home/co60/Documents/python_scripts/advent_of_code/2023/3_text.py'


def coords(y_coord,string) -> tuple[int,None]:
    for i in string:
        first = i.start()
        last = i.end()
        return y_coord, first, last

def intersector(coord_number,coord_spcChr) -> None:
    if coord_number[2] == coord_spcChr[2]:
        print('ejejeje')

y_coord = 0
with open(file) as f:
    lines: list[str] = f.read().splitlines()
    for line in lines:
        specialChr = re.finditer(r'[^\d.]',line)
        number = re.finditer('[0-9]{1,}',line)
        spcCrd = coords(y_coord,specialChr)
        numCrd = coords(y_coord,number)
        print(f'Number : {numCrd}; SpecChr {spcCrd}')
        intersector(numCrd,spcCrd)
        y_coord += 1
