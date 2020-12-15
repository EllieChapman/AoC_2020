last = {
    2: [1,1],
    0: [2,2],
    6: [3,3],
    12: [4,4],
    1: [5,5],
    3: [6,6]
}

consider = 3

for turn in range(7, 30000001):
    if turn % 100000 == 0:
        print(turn)

    spoken = last[consider][0] - last[consider][1]

    if spoken in last:
        last[spoken] = [turn, last[spoken][0]]
    else:
        last[spoken] = [turn, turn]
    consider = spoken

print(spoken)
