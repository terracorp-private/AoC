import pandas as pd
import sys

file = sys.argv[1]

df = pd.read_csv(file, names=['v1','v2'])

def first_part(df):

    df['v3'] = sorted(df['v1'])
    df['v4'] = sorted(df['v2'])
    df['res'] = abs(df['v3'] - df['v4'])
    res = sum(df['res'])
    print(res)


def second_part(df):

    result = []

    for i in df['v1']:
        res = df[df['v2'] == i].count().to_list()
        x = i * res[0]
        
        result.append(x)

    print(sum(result))


second_part(df)

