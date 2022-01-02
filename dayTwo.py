input = open("input.txt")
inputList = input.readlines()

def firstPart():
    x = 0
    depth = 0
    for i in inputList:
        dir = i.split(" ")[0]
        mag = i.split(" ")[1]
        if (dir == "forward"):
            x += int(mag)
        elif(dir == "up"):
            depth -= int(mag)
        elif(dir == "down"):
            depth += int(mag)
    print(x, depth)

def secondPart():
    x = 0
    depth = 0
    aim = 0
    for i in inputList:
        dir = i.split(" ")[0]
        mag = i.split(" ")[1]
        if (dir == "forward"):
            x += int(mag)
            depth +=(aim * int(mag))
        elif(dir == "up"):
            aim -= int(mag)
        elif(dir == "down"):
            aim += int(mag)
    print(x, depth)

firstPart()
secondPart()