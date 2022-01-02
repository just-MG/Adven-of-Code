inputRaw = open("input.txt")
input = inputRaw.readlines()

def firstPart():
    gamma = [0] * 12
    for char in range(1, 12):
        for each in input:
            gamma[char] += int(each[char])
    
    gammaString = ""
    epsilonString = ""
    epsilon = gamma
    a = 0
    for each in gamma:
        if (each) >= len(input)/2:
            each = 1
            epsilon[a] = 0
        else:
            each = 0
            epsilon[a] = 1

        gammaString += str(each)
        epsilonString += str(epsilon[a])
        a += 1

    gammafr =(int((str(int(gammaString))),2))
    epsilonfr =(int((str(int(epsilonString))),2))
    print(epsilonfr * gammafr)

    
    

firstPart()
