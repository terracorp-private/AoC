#!/usr/bin/env python3

helper = []
helper2 = []
res = []
res2 = []

with open ('data_tag3.2.txt') as data:
    data = data.read().splitlines()
    for index in data:
        helper.append(set(index))
        if len(helper) == 3:
            helper2.append(helper)
            helper = []
    for elm in helper2:
        x,z,y = elm
        x.intersection_update(y, z)
        string = ', '.join(x)
        res.append(string)
    print(res)

    for letter in res:
        print(letter)
        if ord(letter) < 97:
            res2.append(ord(letter)-38)
        else:
            res2.append(ord(letter)-96)
    print(sum(res2))
