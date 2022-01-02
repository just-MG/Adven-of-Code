import numpy as np

file = open('input.txt')
input = file.readlines()
board = []

# test = np.zeros((1000, 1000))
# print(test.shape)
# print(test[11, 100])
# a= np.zeros(10)
# print(a.shape)

for i in range(1000):
    board.append([])
    for n in range(1000):
        board[i].append(0)

def assigning(lineArray, dir):
    if (dir == 'x'):
        subtractionx = (lineArray[2] - lineArray[0])
        if 0 < (subtractionx):
            for i in range(lineArray[0], lineArray[0] + 
            subtractionx + 1):
                board[lineArray[1]][i] += 1
        else:
            for i in range(lineArray[0] + subtractionx, lineArray[0] + 1):
                board[lineArray[1]][i] += 1

    elif(dir == 'y'):
        subtractiony = (lineArray[3] - lineArray[1])
        if 0 < subtractiony:
            for i in range(lineArray[1], lineArray[1] + subtractiony + 1):
                board[i][lineArray[0]] += 1
        else:
            for i in range(lineArray[1] + subtractiony, lineArray[1] + 1):
                board[i][lineArray[0]] += 1
    elif(dir == 'd'):
        subtractionx = (lineArray[2] - lineArray[0])
        subtractiony = (lineArray[3] - lineArray[1])
        if 0 < subtractionx:
            if 0 < subtractiony:
                for i in range(subtractiony + 1):
                    board[lineArray[1] + i][lineArray[0]+i] += 1
                #down and right
            else:
                for i in range(abs(subtractiony) + 1):
                    board[lineArray[1] - i][lineArray[0]+i] += 1
                #moving up and right
                pass
        else:
            if 0 < subtractiony:
                for i in range(abs(subtractionx) + 1):
                    board[lineArray[1] + i][lineArray[0] - i] += 1
                #moving down and left
                pass
            else:
                for i in range(abs(subtractionx) + 1):
                    board[lineArray[1] - i][lineArray[0] - i] += 1
                #moving up and left
                pass

def interpretation(line):
    lineArray = line.split(',')
    tmp = lineArray[1].split('->')
    holdTheLastValue = lineArray[2]
    for i in range(1, 3):
        lineArray[i] = tmp[i-1].strip(' ')
    lineArray.append(int(holdTheLastValue.strip('\n')))

    lineArray = list(map(int, lineArray))

    if (lineArray[0] == lineArray[2]):
        assigning(lineArray, 'y')
    elif (lineArray[1] == lineArray[3]):
        assigning(lineArray, 'x')
    elif (abs(lineArray[3] - lineArray[1]) == abs(lineArray[2] - lineArray[0])):
        assigning(lineArray, 'd')


def partOne():
    for each in input:
        interpretation(each)
partOne()

count = 0
for line in board:
    for element in line:
        if int(element) >= 2:
            count += 1
print(count)