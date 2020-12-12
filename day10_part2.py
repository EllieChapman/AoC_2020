def ways(n):
    if n == 1:
        return 2
    elif n == 2:
        return 4
    elif n == 3:
        return 7


f = open('day10_input.txt', 'r')
preinput=f.readlines()

preinput2 = []
for line in preinput:
    preinput2.append(line.replace("\n", ""))

input = [0]
for i in preinput2:
    input.append(int(i))

input.sort()

diffs = []
for i in range(1, len(input)):
    diffs.append(input[i] - input[i-1])
diffs.append(3)

print(diffs)

total = 1

length = 0
for i in range(0, len(diffs)-1):
    if diffs[i] == 3:
        length = 0
    elif diffs[i+1] != 3:
        length = length + 1
    elif diffs[i+1] == 3:
        print(length)
        if length > 0:
            total = total * ways(length)
        length = 0
    else:
        print("incorrect value")

print(total)
