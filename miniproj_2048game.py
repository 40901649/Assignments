'''
This is a 2048 Game!
'''
import random
print("Welcome to the 2048 GAme!")
print("Press 'w' or 'W' to move UP")
print("Press 's' or 'S' to move DOWN")
print("Press 'a' or 'A' to move LEFT")
print("Press 'd' or 'D' to move RIGHT")
masterList = [[0 for i in range(4)] for i in range(4)]

GAMEON = 1
for row in masterList:
    print('\033[1;32;48m ', *row)
while GAMEON:
    key = input("Enter the command (w/s/a/d): ")

    if key in ('w','W'):
        for col1 in range(0,4):
            addDone = [1,1,1,1]
            for row1 in range(0,4):
                if masterList[row1][col1] != 0:
                    for row2 in range(row1,0,-1):
                        if masterList[row2-1][col1]==0:
                            masterList[row2-1][col1], masterList[row2][col1] = masterList[row2][col1], masterList[row2-1][col1]
                        elif masterList[row2-1][col1] == masterList[row2][col1] and addDone[row2-1]:
                            masterList[row2 - 1][col1] *= 2
                            masterList[row2][col1] = 0
                            addDone[row2-1::-1] = [0 for i in range(row2)]

    elif key in ('s','S'):
        for col1 in range(0,4):
            addDone = [1, 1, 1, 1]
            for row1 in range(3, -1, -1):
                if masterList[row1][col1] != 0:
                    for row2 in range(row1, 3):
                        if masterList[row2 + 1][col1] == 0:
                            masterList[row2 + 1][col1], masterList[row2][col1] = masterList[row2][col1], \
                                                                                 masterList[row2 + 1][col1]
                        elif masterList[row2+1][col1] == masterList[row2][col1] and addDone[row2+1]:
                            masterList[row2 + 1][col1] *= 2
                            masterList[row2][col1] = 0
                            addDone[row2+1:] = [0 for i in range(3-row2)]
    elif key in ('a', 'A'):
        for row1 in range(0,4):
            addDone = [1, 1, 1, 1]
            for col1 in range(0,4):
                if masterList[row1][col1] != 0:
                    for col2 in range(col1,0,-1):
                        if masterList[row1][col2-1]==0:
                            masterList[row1][col2-1], masterList[row1][col2] = masterList[row1][col2], masterList[row1][col2-1]
                        elif masterList[row1][col2 - 1] == masterList[row1][col2] and addDone[col2 - 1]:
                            masterList[row1][col2 - 1] *= 2
                            masterList[row1][col2] = 0
                            addDone[col2-1::-1] = [0 for i in range(col2)]

    elif key in('d','D'):
        for row1 in range(0,4):
            addDone = [1, 1, 1, 1]
            for col1 in range(3, -1, -1):
                if masterList[row1][col1] != 0:
                    for col2 in range(col1, 3):
                        if masterList[row1][col2 + 1] == 0:
                            masterList[row1][col2 + 1], masterList[row1][col2] = masterList[row1][col2], \
                                                                                 masterList[row1][col2 + 1]
                        elif masterList[row1][col2 + 1] == masterList[row1][col2] and addDone[col2 + 1]:
                            masterList[row1][col2 + 1] *= 2
                            masterList[row1][col2] = 0
                            addDone[col2+1:] = [0 for i in range(3-col2)]

    else:
        print('Please enter valid key only!')
        continue
    row = random.randint(0, 3)
    col = random.randint(0, 3)
    while masterList[row][col] != 0:
        row = random.randint(0, 3)
        col = random.randint(0, 3)
    masterList[row][col] = 2
    for row11 in range(0,4):
        for col11 in range(0,4):
            if row11 == row  and col11 == col:
                print('\033[1;31;48m ', masterList[row11][col11], end= " ")
            else:
                print('\033[1;32;48m ', masterList[row11][col11], end= " ")
        print("\n")
    GAMEON = 0
    for row in masterList:
        for elem in row:
            if elem == 0:
                GAMEON = 1
