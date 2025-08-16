#!/usr/bin/env python3

test = ['vJrwpWtwJgWrhcsFMMfFFhFp',
 'jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL',
'PmmdzqPrVvPwwTWBwg',
 'wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn',
 'ttgJtRGJQctTZtZT',
'CrZsJsPPZsGzwwsLwLmpwMDw']

h_len = []
res = []

with open ('data_tag3.txt') as data:
    data = data.read().splitlines()
    for item in data:
        lenght = int(len(item)/2)
        h_len = item[lenght:]
        h2_len = item[:-lenght]
        for letter in h_len:
            if letter in h2_len:
                print(letter)
                if ord(letter) < 97:
                    res.append(ord(letter)-38)
                else:
                    res.append(ord(letter)-96)
                break
    print(sum(res))
