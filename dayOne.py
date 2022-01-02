from typing import List


measurements = open("input.txt")
measurementsList = measurements.readlines()

def firstPart(list):
    """
    Accepts a list and returns the number of values that were increased
    """
    count = 0
    for i in range(1, len(list)):
        if list[i] > list[i - 1] :
            count += 1
    print(count)
    return count

def secondPart(): 
    iteration = len(measurementsList) - 2
    list = [];
    for i in range(0, iteration):
        list.append([measurementsList[i].strip("\n"), measurementsList[i+1].strip("\n"), measurementsList[i+2].strip("\n")])
    listOfSums = []
    for i in list:
        listOfSums.append(int(i[0]) + int(i[1]) + int(i[2]))
    firstPart(listOfSums)

secondPart()
