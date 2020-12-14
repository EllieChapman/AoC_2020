f = open('day14_input.txt', 'r')
input=f.readlines()

mem_address = {}


for line in input:
    if line[0:4] == "mask":
        zeros = []
        temp = line[7:]
        for i in range(0, len(temp)):
            if temp[i] == "0":
                ss = "1" + "0" * (len(temp) -i -2)
                num = int(ss, base = 2)
                zeros.append(num)
        j = temp.replace("X", "0")
        mask = int(j, base = 2)
        # print(mask)
        # print(zeros)
    else:
        # have a mem write instruction
        temp = line.replace("\n", "").split("]")
        mem = temp[0][4:]
        # print(mem)
        value = int(temp[1][3:])
        # print(value)

        value = value | mask
        # print("value",value)

        for i in zeros:
            if value & i:
                value = value - i
        # print("final", value)

        mem_address[mem] = value

total = 0
for key in mem_address:
    total = total + mem_address[key]

print(total)
