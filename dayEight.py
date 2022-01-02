import time

with open("input.txt") as f:
    lines = f.readlines()

i = 0
for entry in lines:
    entry = entry.strip('\n').split("|")
    entry[0] = entry[0].split(' ')
    entry[0].remove('')
    entry[1] = entry[1].split(' ')
    entry[1].remove('')
    lines[i] = entry
    i += 1

def partOne():
    count = 0
    for line in lines:
        for i in range(len(line[1])):
            line[1][i] = len(line[1][i])
        count += (line[1].count(7) + line[1].count(2) + line[1].count(3) + line[1].count(4))
    print(count)

def partTwo():
# 1 -> always when has 2 lines
# 2 -> always when has 5 lines, 2 of them are conv with 3 and is not conv with 1
# 3 -> when 5 lines, 2 of them are conv with 1
# 4 -> always when 4 lines
# 5 -> when 5 lines, 3 are conv with 4, is not conv with 1
# 6 -> when 6 lines, all of them are conv with 8 and is not conv with 1
# 7 -> when is 3 lines
# 8 -> when is 7 lines
# 9 -> when 6 lines and all conv with 8 and 4
# 0 -> when has 6 lines, all conv with 8 and not with 4
# 
# first count the letters, then go to the detailed cases on what can that be - 
    bigSum = []
    for entry in lines:
        nums = {1: "", 2: "", 3: "", 4: "", 5: "", 6: "", 7: "", 8: "", 9:"", 0: ""}
        while(nums[0] == "" or nums[1] == ""  or nums[2] == "" or nums[4] == "" or nums[3] == "" or nums[5] == "" or nums[6] == "" or nums[7] == "" or nums[8] == "" or nums[9] == ""):
            for element in entry[0]:
                tmp = len(element)
                # the four easy cases
                if tmp == 4:
                    nums[4] = element
                elif tmp == 2:
                    nums[1] = element
                elif tmp == 7:
                    nums[8] = element
                elif tmp == 3:
                    nums[7] = element
                elif tmp == 6:
                    #the six - letter long ones
                    # they include 0, 6 and 9
                    if (nums[8] != "" and nums[4] != "" and nums[1] != ""):
                        # 9
                        countInEight = 0
                        for each in element:
                            if nums[8].find(each) >= 0: countInEight += 1
                        countInFour = 0
                        for each in element:
                            if nums[4].find(each) >= 0: countInFour += 1
                        countInOne = 0
                        for each in element:
                            if nums[1].find(each) >= 0: countInOne += 1
                        if countInEight == len(element) and countInFour == len(nums[4]): 
                            nums[9] = element
                        # 0
                        if (countInEight == len(element) and countInFour != len(nums[4]) and countInOne == len(nums[1])):
                            nums[0] = element
                        # 6
                        if (countInEight == len(element) and countInOne != len(nums[1])):
                            nums[6] = element
                elif tmp == 5:
                    #the five letter long ones
                    #they include 2, 3 and 5
                    countInOne = 0
                    for each in element:
                        if nums[1].find(each) >= 0: countInOne += 1
                    # 3
                    if countInOne == 2:
                        nums[3] = element
                    if (nums[3]!= ""):
                        countInThree = 0
                        for each in element:
                            if nums[3].find(each): countInThree += 1
                        countInFour = 0
                        for each in element:
                            if nums[4].find(each) >= 0: countInFour += 1
                        countInOne = 0
                        for each in element:
                            if nums[1].find(each) >= 0: countInOne += 1
                        # 2
                        if (countInOne != 2) and (countInFour != 3):
                            nums[2] = element
                    if (nums[4] != "" and nums[1] != ""):
                        countInFour = 0
                        for each in nums[4]:
                            if element.find(each) >= 0: countInFour += 1
                        countInOne = 0
                        for each in element:
                            if nums[1].find(each) >= 0: countInOne += 1
                        # 5
                        if (countInFour == 3 and countInOne != len(nums[1])):
                            nums[5] = element
                    pass        
        print(nums)
        key_list = list(nums.keys())
        val_list = list(nums.values())
        val = ""
        for each in entry[1]:
            for element in nums:
                count = 0
                for char in each:
                    if nums[element].find(char) >= 0: count += 1
                if (count == len(each)) and (len(nums[element]) == len(each)):
                    tmp = nums[element]
                    position = val_list.index(tmp)
                    val += str((key_list[position]))
                    break
        bigSum.append(int(val))
    sum = 0
    for each in bigSum:
        sum += each
    print(sum)
    return sum

partTwo()
