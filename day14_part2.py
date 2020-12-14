def perm(n):
    perms = []
    for i in range(0, pow(2,n)):
        code = "#0" + str(n+2) + "b"
        perms.append(format(i, code)[2:])
    return(perms)
    

f = open('day14_input.txt', 'r')
input=f.readlines()

mem_address = {}

for line in input:
    if line[0:4] == "mask":
        premask = line[7:]
        mask = ""
        for i in range(0, len(premask)-1):
            if premask[i] != "X":
                mask = mask + premask[i]
            else:
                mask = mask + "0"
        mask = int(mask, base=2)

        x_pos = []
        for i in range(0, len(premask)):
            if premask[i] == "X":
                x_pos.append(i)

        perms = perm(len(x_pos))

    else:
        temp = line.replace("\n", "").split("]")
        mem = int(temp[0][4:])
        value = int(temp[1][3:])

        mem = mem | mask

        code = "#0" + str(38) + "b"
        mem = (format(mem, code)[2:])

        for i in perms:
            final_mem = mem
            for j in range(0, len(x_pos)):
                final_mem = final_mem[0:x_pos[j]] + i[j] + final_mem[x_pos[j]+1:]
            mem_address[final_mem] = value

total = 0
for key in mem_address:
    total = total + mem_address[key]
print(total)
