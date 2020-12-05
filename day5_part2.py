f = open('day5_input.txt', 'r')
input=f.read()

input = input.replace("F", "0")
input = input.replace("B", "1")
input = input.replace("L", "0")
input = input.replace("R", "1")

input = input.split("\n")

id = []

for ii in input:
    num = aa = int(ii, base=2)
    id.append(num)

id.sort()

for i in range(0, len(id)-1):
    if id[i+1] - id[i] != 1:
        print(id[i]+1)
