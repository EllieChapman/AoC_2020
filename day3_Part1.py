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


x = 0
y = 0
arrived = 0
tree_count = 0

while arrived == 0:
    coord = str(x) + "," + str(y)
    if tree_dict[coord] == "#":
        tree_count = tree_count + 1
    x = x + 3
    y = y + 1
    if y > (rows-1):
        arrived = 1
    if x > (columns-1):
        x = x-columns

print(tree_count)
