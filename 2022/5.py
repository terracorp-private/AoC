#!/usr/bin/env python 3

import pandas as pd

COLUMNS = [pos for pos in range(1,11)]
pos = pd.read_csv("~/programs/python_files/advent_of_code/data_5_initial_position.csv",names=COLUMNS)
MOV = pd.read_csv("~/programs/python_files/advent_of_code/data_5_movements.csv")

print(pos,'\n',MOV)

# make a list form the datafame. It is a list of a lists
pos = [pos[col].tolist() for col in pos.columns]

# remove nans from the list
posnew = []
for i in pos:
    i = [x for x in i if str(x) != 'nan']
    posnew.append(i)

def move_instructions():
    for _,row in MOV.iterrows():
        n_crates = row['move']
        frm_pointer = row['from'] - 1
        to_pointer = row['to'] - 1
        
        for i in range(n_crates):
            v = posnew[frm_pointer]
            v = v[0]
            posnew[frm_pointer].remove(v)
            posnew[to_pointer].insert(0,v)
    print(posnew)

bulk_list = []
def move_instructions_bulk():
    for _,row in MOV.iterrows():
        n_crates = row['move']
        frm_pointer = row['from'] - 1
        to_pointer = row['to'] - 1
        print(type(n_crates))
       
        crates = posnew[0:n_crates]
        print(crates)
        input()

    print(posnew)

move_instructions_bulk()



