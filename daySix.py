import time

f = open("input.txt", 'r')
input = f.readline().strip(' ').split(",")

#set by hand

# input = list(map(int, input))
# time.process_time()
# time()

# def operation(x):
#     x = [9, x - 1][x >= 1]
#     if (x == 9):
#         input.append(9)
#         x = 6
#     return x

# print(input)
# numberOfDays = 256
# for i in range(numberOfDays):
#     input = (list(map(operation,input)))
#     print("["+"⎕"*int(i/3) + "'"*int((numberOfDays - i)/3) + "]" + f"({(i/numberOfDays * 100)}%)")
#     #print(f"{i + 1} day = {input}")
# print(len(input))

input = list(map(int, input))

currentDay = {
    0: input.count(0),
    1: input.count(1),
    2: input.count(2),
    3: input.count(3),
    4: input.count(4),
    5: input.count(5),
    6: input.count(6),
    7: input.count(7),
    8: input.count(8)
}

nextDay = {}
numberOfDays = 256
for i in range(numberOfDays):
    nextDay = {
        0 : currentDay[1],
        1 : currentDay[2],
        2 : currentDay[3],
        3 : currentDay[4],
        4 : currentDay[5],
        5 : currentDay[6],
        6 : currentDay[7],
        7 : currentDay[8],
        8 : currentDay[0]
    }
    if currentDay[0] > 0: nextDay[6] += currentDay[0]
    currentDay = nextDay

count = 0

for each in currentDay:
    count += currentDay[each]
print(count)
