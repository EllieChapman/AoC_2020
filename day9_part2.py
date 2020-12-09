f = open('day9_input.txt', 'r')
preinput=f.readlines()

input = []
for line in preinput:
    line.replace("\n", "")
    line = int(line)
    input.append(line)

target = 400480901

for ii in range(0, len(input)):
    length = 2
    correct = False
    while correct == False:
        if sum(input[ii:ii+length]) == target:
            contig = input[ii:(ii+length)]
            print( max(contig) + min(contig) )
            correct = True
        elif sum(input[ii:ii+length]) > target:
            break
        elif (ii+length) == len(input):
            break
        else:
            length = length + 1
            continue
