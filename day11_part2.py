def one(row, column):
    hit = False
    while hit == False:
        if row >= 1 and column >= 1:
            if input[row-1][column-1] == "#":
                return 1
            if input[row-1][column-1] == "L":
                return 0
        else:
            return 0
        row = row -1
        column = column -1

def two(row, column):
    hit = False
    while hit == False:
        if row >= 1:
            if input[row-1][column] == "#":
                return 1
            if input[row-1][column] == "L":
                return 0
        else:
            return 0
        row = row -1

def three(row, column):
    hit = False
    while hit == False:
        if row >= 1 and column <= columns-3:
            if input[row-1][column+1] == "#":
                return 1
            if input[row-1][column+1] == "L":
                return 0
        else:
            return 0
        row = row -1
        column = column +1

def four(row, column):
    hit = False
    while hit == False:
        if column <= columns-3:
            if input[row][column+1] == "#":
                return 1
            if input[row][column+1] == "L":
                return 0
        else:
            return 0
        column = column +1

def five(row, column):
    hit = False
    while hit == False:
        if row <= rows-2 and column <= columns-3:
            if input[row+1][column+1] == "#":
                return 1
            if input[row+1][column+1] == "L":
                return 0
        else:
            return 0
        row = row +1
        column = column +1

def six(row, column):
    hit = False
    while hit == False:
        if row <= rows-2:
            if input[row+1][column] == "#":
                return 1
            if input[row+1][column] == "L":
                return 0
        else:
            return 0
        row = row +1

def seven(row, column):
    hit = False
    while hit == False:
        if row <= rows-2 and column >= 1:
            if input[row+1][column-1] == "#":
                return 1
            if input[row+1][column-1] == "L":
                return 0
        else:
            return 0
        row = row +1
        column = column -1

def eight(row, column):
    hit = False
    while hit == False:
        if column >= 1:
            if input[row][column-1] == "#":
                return 1
            if input[row][column-1] == "L":
                return 0
        else:
            return 0
        column = column -1


def change(row, column, state):
    occupied = 0

    occupied = occupied + one(row, column)
    occupied = occupied + two(row, column)
    occupied = occupied + three(row, column)
    occupied = occupied + four(row, column)
    occupied = occupied + five(row, column)
    occupied = occupied + six(row, column)
    occupied = occupied + seven(row, column)
    occupied = occupied + eight(row, column)


    # print(occupied)
    if state == "L" and occupied == 0:
        # print(occupied)
        return True
    elif state == '#' and occupied >= 5:
        # print(occupied)
        return True
    else:
        return False


def changing():
    for x in range(0, columns -1):
        for y in range(0, rows):
            # print(x,y, input[y][x])
            if change(y,x, input[y][x]) == True:
                # print("change")
                return True
    return False



f = open('day11_input.txt', 'r')
input=f.readlines()

rows = len(input)
columns = len(input[0])

# print(rows, columns)

changes = True

while changes == True:
    changes = changing()

    string_val = ""
    temp_list = []
    for i in range(0, rows):
        temp_list.append(string_val)

    for x in range(0, columns -1):
        for y in range(0, rows):
            # print(x,y, input[y][x])
            if change(y,x, input[y][x]) == True:
                # print("change")
                if input[y][x] == "L":
                    temp_list[y] = temp_list[y] + "#"
                else:
                    temp_list[y] = temp_list[y] + "L"
            else:
                # print("stay")
                temp_list[y] = temp_list[y] + input[y][x]
    # for i in temp_list:
    #     print(i)
    input = temp_list.copy()

total = 0
for i in temp_list:
    for char in i:
        if char == "#":
            total = total + 1
print(total)
