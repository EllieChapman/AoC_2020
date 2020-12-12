f = open('day10_input.txt', 'r')
preinput=f.readlines()

preinput2 = []
for line in preinput:
    preinput2.append(line.replace("\n", ""))

input = [0]
for i in preinput2:
    input.append(int(i))

input.sort()

# print(input)

diff1 = 0
diff2 = 0
diff3 = 1

for i in range(1, len(input)):
    if input[i] - input[i-1] == 1:
        diff1 = diff1 + 1
    elif input[i] - input[i-1] == 2:
        diff2 = diff2 + 1
    else:
        diff3 = diff3 + 1

print(diff1*diff3)
