#!/usr/bin/env python3

import sys

FILE: str = sys.argv[1]

area_sum: list[int] = []
with open(FILE) as data:
    for _, line in enumerate(data):
        dimentions: list[str] = line.split('x')
        l: int = int(dimentions[0])
        w: int = int(dimentions[1])
        h: int = int(dimentions[2])
        (smallest_side_area := min([l*w,w*h,h*l]))
        area: int = (2*l*w + 2*w*h + 2*h*l) + smallest_side_area
        area_sum.append(area)
    result: int = sum(area_sum)
    print(result)
