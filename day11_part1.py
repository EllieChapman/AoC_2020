def change(row, column, state):
    occupied = 0
    if row >= 1 and column >= 1:
        if input[row-1][column-1] == "#":
            occupied = occupied + 1
    if row >= 1:
        if input[row-1][column] == "#":
            occupied = occupied + 1
    if row >= 1 and column <= columns-3:
        if input[row-1][column+1] == "#":
            occupied = occupied + 1
    if column <= columns-3:
        if input[row][column+1] == "#":
            occupied = occupied + 1
    if row <= rows-2 and column <= columns-3:
        if input[row+1][column+1] == "#":
            occupied = occupied + 1
    if row <= rows-2:
        if input[row+1][column] == "#":
            occupied = occupied + 1
    if row <= rows-2 and column >= 1:
        if input[row+1][column-1] == "#":
            occupied = occupied + 1
    if column >= 1:
        if input[row][column-1] == "#":
            occupied = occupied + 1
    # print(occupied)
    if state == "L" and occupied == 0:
        # print(occupied)
        return True
    elif state == '#' and occupied >= 4:
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
