f = open('day9_input.txt', 'r')
preinput=f.readlines()

input = []
for line in preinput:
    line.replace("\n", "")
    line = int(line)
    input.append(line)

# print(input)


for ii in range(25, len(input)):
    correct = False
    while correct == False:
        for no1 in range(ii-25, ii):
            for no2 in range(ii-24, ii-1):
                if input[no1] + input[no2] == input[ii]:
                    correct = True
        if correct == False:
            print(input[ii])
            break
