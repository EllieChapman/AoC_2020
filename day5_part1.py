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

print(max(id))
