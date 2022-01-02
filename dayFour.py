inputRaw = open("input.txt")
firstLine = inputRaw.readline()
drawnNums = firstLine.strip("\n").split(",")
boards = []

for i in range(0, 100):
    inputRaw.readline()
    tmp = []
    for line in range(0,5):
        tmp.append(inputRaw.readline().strip("\n").split(" "))
    boards.append(tmp)
for each in boards:
    print(each)
print("#"*10)

def checkRows(alreadyDrawnNums):
    x = 0
    wonBoards = []
    for board in boards:
        x += 1
        for row in range(0, len(board)): #breaking down to single rows
            count = 0
            for num in range(0, len(board[row])): #checking each digit in the row
                for i in alreadyDrawnNums: #checking for each already drawn number, if i
                    try:
                        if int(i) == int(board[row][num]):
                            count += 1
                    except:
                        print("sth wrong")
            if count == len(board[row]):
                print("board", x, "wins, after", len(alreadyDrawnNums), "numbers being drawn. These are: ")
                print(', '.join(alreadyDrawnNums)) 
                print(f"The row that won was {row + 1}")
                wonBoards.append(board)

                
                # this only finds the first board that wins after drawing the nums, you need to add the index of the board that wins to a general winners list and then a) remove these boards and then b) return that more than one board 
    print(len(wonBoards))
    if (len(wonBoards) != 0):
        for element in wonBoards:
            print(element[0:4])
            boards.remove(element)
        print("rows checked")
        return True, wonBoards,x
    else:
        print("rows checked (f)")
        return False, [], x
    
    

def checkColumns(alreadyDrawnNums):
    x = 0
    wonBoards= []
    for board in boards:
        x += 1
        for column in range(5):
            count = 0
            for row in range(5):
                for i in alreadyDrawnNums:
                    try:
                        if int(i) == int(board[row][column]):
                            count += 1
                    except:
                        pass
            if count == 5:
                print("board", x, "wins, after", len(alreadyDrawnNums), "numbers being drawn. These are: ")
                print(', '.join(alreadyDrawnNums))
                print(f"The column that won was {column + 1}")
                wonBoards.append(board)
    if (len(wonBoards) != 0):
        print("entered the winning if")
        for board in wonBoards:
            for row in board:
                print(row)
            print('-'*10)
        boards.remove(board)
        print("cols checked")
        return True, wonBoards,x 
    else:
        print("cols checked (f)")
        return False, [], x

def countingPoint(wonBoards, alreadyDrawnNums):
    score = 0
    for board in wonBoards:
        for row in board:
            for each in alreadyDrawnNums:
                try:
                    row.remove(each)
                except:
                    pass
            for element in row:
                score += int(element)
    print(wonBoards[0:4])
    tmp = int((alreadyDrawnNums[len(alreadyDrawnNums) - 1]))
    print(score)
    score = score * tmp
    print(f"score: {score}")
        
def partOne():            
    alreadyDrawnNums = []
    y = 0
    for a in drawnNums:
        y += 1
        currentNum = a
        alreadyDrawnNums.append(currentNum)

        cols = checkColumns(alreadyDrawnNums)
        rows = checkRows(alreadyDrawnNums)
        if (cols[0] == True):
            i = 0
            for each in cols[1]:
                print(f"board {i+1} = ")
                for board in each:
                    print(board)
                i +=1
            print("win by columns")
            countingPoint(cols[1], alreadyDrawnNums)
            
        elif (rows[0] == True):
            i = 0
            for each in cols[1]:
                print(f"board {i+1} = ")
                for board in each:
                    print(board)
                i +=1
            print("win by rows")
            countingPoint(rows[1], alreadyDrawnNums)

        
        print(f"boards left {len(boards)}, number of iteratons: {y}")
        print("#"*30)

    
# so the output says that one board is constatny winning and that\s because the boards are changing positions. Now in order to find the sum of the winning board i will need to calculate the board that is left (and is being said to be the winner). Look at the note created, it will show you what happened there.
# 
# Apparently there's a method consists that could check each row individually, comparing it to the numbers that were alreasdy drawn     
partOne()

