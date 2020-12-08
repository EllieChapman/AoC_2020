def check(input):
    accumulator = 0
    pointer = 0
    visited = []
    repeat = False

    while repeat == False:
        if pointer in visited:
            return False
        elif pointer >= len(input):
            print(accumulator)
            return True
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


f = open('day8_input.txt', 'r')
preinput=f.readlines()

input = []
for rule in preinput:
    rule = rule.replace("\n", "")
    instruct = rule.split(" ")
    input.append(instruct)


for line in range(0, len(input)):
    if input[line][0] == "nop":
        input[line][0] = "jmp"
        if check(input) == True:
            break
        else:
            input[line][0] = "nop"
            continue

    elif input[line][0] == "jmp":
        input[line][0] = "nop"
        if check(input) == True:
            break
        else:
            input[line][0] = "jmp"
            continue
