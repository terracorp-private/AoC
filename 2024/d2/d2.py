import sys
import numpy as np


def monotony(seq):
    '''check for monotony of a seq'''    

    if (np.all(np.diff(seq) > 0) or np.all(np.diff(seq) < 0)):
        return True

    else:
        return False

def distance(seq):
    '''check whether an aboslute value of two adjacent numbers is 1 <= x <= 3''' 

    for idx in range(1, len(seq)):
        absolut_value = abs(seq[idx] - seq[idx - 1])

        if not ((1 <= absolut_value) and (absolut_value <= 3)):
            return False

    return True


def heilMacher(seq):
    
    if (monotony(seq) and distance(seq)):
        return seq

    else:
        for i in range(len(seq)):
            short_seq = seq.copy()
            del short_seq[i]

            if (monotony(short_seq) and distance(short_seq)):
                return seq
                


file = sys.argv[1]

with open(file) as data:

    count = 0

    for line in data:

        sequence = list(map(int, line.split()))

        matched_sequence = heilMacher(sequence)        
        
        if matched_sequence is not None:
            count += 1


print(count)



