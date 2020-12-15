last = {
    2: [1],
    0: [2],
    6: [3],
    12: [4],
    1: [5],
    3: [6]
}

consider = 3

for turn in range(7, 2021):
    if len(last[consider]) == 1:
        spoken = 0
    else:
        spoken = last[consider][0] - last[consider][1]

    if spoken in last:
        last[spoken] = [turn] + last[spoken]
    else:
        last[spoken] = [turn]
    consider = spoken

print(spoken)
