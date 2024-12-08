import sys
import re

file = sys.argv[1]


def multInstruction(lines):


    resultSum = 0
    
    for line in lines:
        instructions = re.findall(r'mul\(\d*,\d*\)', line) 

        for instruction in instructions:
            
            number = instruction.lstrip('mul(')
            number = number.rstrip(r')')
            firsNumber = int(number.split(',')[0])
            secondNumber = int(number.split(',')[1])

            resultProduct = firsNumber * secondNumber
            resultSum = resultSum + resultProduct
            
            # print(instruction, number, firsNumber, secondNumber, sep='\t')

    return resultSum


with open(file) as data:

    reportString = data.readlines()
   
    print(multInstruction(reportString))
     

