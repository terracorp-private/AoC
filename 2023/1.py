#!/usr/bin/env python

import re

calibration_document = '/home/alpha/programs/python_files/advent_of_code/2023/d1.txt'

strNums = {'one':'1','two':'2', 'three':'3',
           'four':'4', 'five':'5', 'six':'6',
           'seven':'7', 'eight':'8', 'nine':'9'}

sumList = []
with open(calibration_document) as cd:
    for row in cd:
        numbers = re.findall('(?=(one|two|three|four|five|six|seven|eight|nine|\d))',row)
        n1 = numbers[0]
        n2 = numbers[-1]

        if n1 in strNums:
            n1 = strNums[n1]
        if n2 in strNums:
            n2 = strNums[n2]

        nConcat = str(n1) + str(n2)
        nConcat = int(nConcat)
        sumList.append(nConcat)
    print(sum(sumList))
