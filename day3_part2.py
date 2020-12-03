import math

f = open('day3_input.txt', 'r')
positions=f.read()

rows = 1
columns = 0

for character in positions:
    if character == "\n":
        rows = rows + 1
for character in positions:
    if character != "\n":
        columns = columns + 1
    else:break
print("rows", rows, " ", "columns", columns)

positions = positions.replace("\n", "")

tree_dict = {}

for ii in range(0, len(positions)):
    x = ii%columns
    y = math.trunc(ii/columns)
    coord = str(x) + "," + str(y)
    tree_dict[ coord ] = positions[ii]


xs = [1,3,5,7,1]
ys = [1,1,1,1,2]
counts = []

for i in range(0,5):
    tree_count = 0
    x = 0
    y = 0
    arrived = 0
    while arrived == 0:
        coord = str(x) + "," + str(y)
        if tree_dict[coord] == "#":
            tree_count = tree_count + 1
        x = x + xs[i]
        y = y + ys[i]
        if y > (rows-1):
            arrived = 1
        if x > (columns-1):
            x = x-columns
    counts.append(tree_count)

total = 1
for i in counts:
    total = total * i

print(total)
