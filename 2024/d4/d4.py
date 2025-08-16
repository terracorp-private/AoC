import sys




def matrixMaker(lines):
    

    yCoordX = 0
    yCoordM = 0
    yCoordA = 0
    yCoordS = 0

    matrxCoordX = []
    matrxCoordM = []
    matrxCoordA = []
    matrxCoordS = []


    for line in lines:

        if 'X' in line:
            xCoordX = [pos for pos, char in enumerate(line) if char == 'X']
            # yCoordX += 1
            matrxCoordX.append(xCoordX)


        if 'M' in line:
            xCoordM = [pos for pos, char in enumerate(line) if char == 'M']
            matrxCoordM.append(xCoordM)
            # yCoordM += 1


        if 'A' in line:
            xCoordA = [pos for pos, char in enumerate(line) if char == 'A']
            matrxCoordA.append(xCoordA)
            # yCoordA += 1


        if 'S' in line:
            xCoordS = [pos for pos, char in enumerate(line) if char == 'S']
            matrxCoordS.append(xCoordS)
            # yCoordS += 1

    # print(matrxCoordX)
    return matrxCoordX, matrxCoordM, matrxCoordA, matrxCoordS


pth = sys.argv[1]

with open(pth) as file:


    data = file.readlines()

    
    x = matrixMaker(data)[1]

    for row in x:
        for char in row:
            print(char)


