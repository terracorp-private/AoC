#!/usr/bin/env python

import re

# CONDITION: 12 red cubes, 13 green cubes, and 14 blue cubes

data = '/home/alpha/programs/python_files/advent_of_code/2023/d2.txt'


gameID_sum = 0
sum_of_set_powers = 0

def gem_color_addition(color,gems):
    helperMIN = []
    for gem in gems:
        gem = gem.replace(color,'')
        gem = int(gem)
        helperMIN.append(gem)
    gem = max(helperMIN)
    return gem


with open(data) as data:
    games = data.read().splitlines()
    for game in games:
        # print(game)
        game = game.replace(' ','')
        game = game.replace(':',';')
        gameID = game.split(';')[0]
        stone = game.split(';')[1::]


 # checking, whether the sum of the stones satisfies the condition

        # print('game ID: ', gameID)
        stone = ','.join(stone)
        red = re.findall('[0-9]{1,}red',stone)
        green = re.findall('[0-9]{1,}green',stone)
        blue = re.findall('[0-9]{1,}blue',stone)

        allred = gem_color_addition('red',red)
        allgreen = gem_color_addition('green',green)
        allblue = gem_color_addition('blue',blue)

        # print(f'before the filtering red {allred}, green {allgreen}, blue {allblue}') 
      

        # PART 1
        # if (allred <= 12) and (allgreen <= 13) and (allblue <= 14):
        #     gameID = gameID.replace('Game','')
        #     gameID_Int = int(gameID)
        #     gameID_sum = gameID_sum + gameID_Int
        #     print(f'after the filtering red {allred}, green {allgreen}, blue {allblue}') 
        #     print(gameID_sum)
        

        # PART 2
        set_power = allred * allgreen * allblue
        sum_of_set_powers = sum_of_set_powers + set_power
        print(sum_of_set_powers)


