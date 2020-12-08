f = open('day8_input.txt', 'r')
preinput=f.readlines()

input = []
for rule in preinput:
    rule = rule.replace("\n", "")
    instruct = rule.split(" ")
    input.append(instruct)

print(input[0][0])

accumulator = 0
pointer = 0
visited = []
repeat = False

while repeat == False:
    if pointer in visited:
        print(accumulator)
        repeat = True
    else:
        visited.append(pointer)
        if input[pointer][0] == "nop":
            pointer = pointer + 1
        elif input[pointer][0] == "acc":
            accumulator = accumulator + int(input[pointer][1])
            pointer = pointer + 1
        elif input[pointer][0] == "jmp":
            pointer = pointer + int(input[pointer][1])
        else:
            print("unrecognised input")
