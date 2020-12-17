f = open('day17_input.txt', 'r')
input=f.readlines()

def cmc(n):
    a = n.split(",")
    b = []
    for i in a:
        b.append(int(i))
    return b


active = [ [3, 1, 1], [4, 1, 1], [6, 1, 1], [8, 1, 1], [1, 0, 1], [2, 0, 1], [7, 0, 1], [5, -1, 1], [6, -1, 1], [7, -1, 1], [8, -1, 1], [1, -2, 1], [4, -2, 1], [5, -2, 1], [1, -3, 1], [4, -3, 1], [6, -3, 1], [7, -3, 1], [2, -4, 1], [5, -4, 1], [1, -5, 1], [2, -5, 1], [6, -5, 1], [7, -5, 1], [2, -6, 1], [6, -6, 1] ]

for turn in range(0, 6):
    dict = {}

    for cube in active:
        for x in range(cube[0]-1, cube[0]+2):
            for y in range(cube[1]-1, cube[1]+2):
                for z in range(cube[2]-1, cube[2]+2):
                    if x == cube[0] and y == cube[1] and z == cube[2]:
                        continue
                    ss = str(x)+ "," + str(y)+ "," + str(z)
                    if ss in dict:
                        dict[ss] = dict[ss]+1
                    else:
                        dict[ss] = 1
    new_active = []
    for key in dict:
        # print(key, dict[key])
        if dict[key] == 3:
            new_active.append(cmc(key))
        elif dict[key] == 2 and cmc(key) in active:
            new_active.append(cmc(key))

    active = new_active

print(len(active))
