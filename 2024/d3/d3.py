import sys
import re
import pandas as pd

file = sys.argv[1]



def multInstruction(data):


    resultSum = 0
    
    instructions = re.findall(r'mul\(\d*,\d*\)', data) 
   
    for instruction in instructions:
        
        number = instruction.lstrip('mul(')
        number = number.rstrip(r')')
        firsNumber = int(number.split(',')[0])
        secondNumber = int(number.split(',')[1])

        resultProduct = firsNumber * secondNumber
        resultSum = resultSum + resultProduct
        

    return resultSum


def clearRAM(data):
    

    instrList = re.findall(r'(don\'t\(\)|mul\(\d*,\d*\)|do\(\))', data)
    mult = re.findall(r'mul\(\d*,\d*\)', data) 
    do = re.findall(r'do\(\)', data) 
    dont = re.findall(r'don\'t\(\)', data) 
   
    return instrList
        
    

def tunedInstr(data):

    mult = re.findall(r'mul\(\d*,\d*\)', data) 
    return mult


with open(file) as f:


    dataRaw = f.read()


    print(multInstruction(dataRaw))
    # df = pd.DataFrame({'Instrunctions': clearRAM(dataRaw)})
    # df.to_csv('clearedData.csv', index=False)
   

# answer_part2 = 113965544
