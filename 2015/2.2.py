#!/usr/bin/env python3


#!/usr/bin/env python3

import sys

FILE: str = sys.argv[1]

ribbon_sum: list[int] = []
with open(FILE) as data:
    for _, line in enumerate(data):
        l: int = int(line.split('x')[0])
        w: int = int(line.split('x')[1])
        h: int = int(line.split('x')[2])
        dimentions = [l,w,h]
        dimentions.sort()
        perimeter1 = dimentions[0] + dimentions[0]
        perimeter2 = dimentions[1] + dimentions[1]
        ribbon = perimeter1 + perimeter2
        bow: int = (l*w*h)
        ribbon_total: int = ribbon + bow
        ribbon_sum.append(ribbon_total)
    result: int = sum(ribbon_sum)
    print(result)
