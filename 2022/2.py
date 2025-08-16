#!/usr/bin/env python3

#A for Rock, B for Paper, and C for Scissors
#X for Rock, Y for Paper, and Z for Scissors

# B Z
# A Z
# B Z
# C Z
# C Z
# B X
# A X
# C X
# A Z
# C Y

test_list = ['A Y', 'B X', 'C Z']

helper = []

with open ('data_tag2.txt') as f:
    lines = f.read().splitlines()

A = 1
B = 2
C = 3

X = 1
Y = 2
Z = 3

# X = lose
# Y = draw
# Z = win

# for item in lines:
#     # DRAW
#     if item == 'A X':
#         helper.append(3 + X)
#     elif item == 'B Y':
#         helper.append(3 + Y)
#     elif item == 'C Z':
#         helper.append(3 + Z)
#     # LOSS
#     elif item == 'A Z':
#         helper.append(0 + Z)
#     elif item == 'B X':
#         helper.append(0 + X)
#     elif item == 'C Y':
#         helper.append(0 + Y)
#     # WIN
#     elif item == 'A Y':
#         helper.append(6 + Y)
#     elif item == 'B Z':
#         helper.append(6 + Z)
#     else:
#         helper.append(6 + X)
# print(sum(helper))

for item in lines:
    # LOSE
    if item == 'A X':
        helper.append(0 + Z)
    elif item == 'B X':
        helper.append(0 + X)
    elif item == 'C X':
        helper.append(0 + Y)
    # DRAW
    elif item == 'A Y':
        helper.append(3 + X)
    elif item == 'B Y':
        helper.append(3 + Y)
    elif item == 'C Y':
        helper.append(3 + Z)
    # WIN
    elif item == 'A Z':
        helper.append(6 + Y)
    elif item == 'B Z':
        helper.append(6 + Z)
    else:
        helper.append(6 + X)
print(sum(helper))

# #draw condition
# A + X = 3 + X
# B + Y = 3 + Y
# C + Z = 3 + Z

# #loss condition
# A + Z = 0 + Z
# B + X = 0 + X
# C + Y = 0 + Y

# #win condition
# A + Y = 6 + Y
# B + Z = 6 + Z
# C + X = 6 + X
