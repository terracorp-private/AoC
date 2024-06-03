#!/usr/bin/env python3

import sys

FILE: str = sys.argv[1]

def santa_moves(line: list[str]) -> set:
    x: int = 0
    y: int = 0
    santa_trail: list[int] = []
    for turn, movement in enumerate(line):
        if movement == '^':
            y += 1
        elif movement == 'v':
            y -= 1
        elif movement == '>':
            x += 1
        else:
            x -= 1
        coords: tuple(int,int) = (x,y)
        santa_trail.append(coords)
    houses: set = set(santa_trail)
    return houses

def robo_santa_moves(line: list[str]) -> set:
    x: int = 0
    y: int = 0
    xr : int = 0
    yr : int = 0
    santa_trail: list[int] = []
    robo_santa_trail: list[int] = []
    for turn, movement in enumerate(line):
        if turn % 2 == 0:
            if movement == '^':
                y += 1
            elif movement == 'v':
                y -= 1
            elif movement == '>':
                x += 1
            else:
                x -= 1
            coords: tuple(int,int) = (x,y)
            santa_trail.append(coords)
        else:
            if movement == '^':
                yr += 1
            elif movement == 'v':
                yr -= 1
            elif movement == '>':
                xr += 1
            else:
                xr -= 1
            robo_coords: tuple(int,int) = (xr,yr)
            robo_santa_trail.append(robo_coords)
    santa: set = set(santa_trail)
    robo_santa: set = set(robo_santa_trail)
    houses: set = santa.union(robo_santa)
    return houses


with open(FILE) as data:
    line: str = data.readline()
    santa_visited_houses: int = len(santa_moves(line))
    robosanta_visited_houses: int = len(robo_santa_moves(line))
    print(santa_visited_houses, robosanta_visited_houses)
