f = open('day18_input.txt', 'r')
preinput=f.readlines()

input = []
for i in preinput:
    j = i.replace("(", "( ").replace(")", " )").replace("\n", "")
    k = j.split(" ")
    input.append(k)

def sum(l):
    # print(l)
    while len(l) > 2:
        if l[1] == "+":
            s = int(l[0]) + int(l[2])
            if len(l) >= 5:
                l = [str(s)] + l[3:]
            else:
                return [str(s)]
        elif l[1] == "*":
            s = int(l[0]) * int(l[2])
            if len(l) >= 5:
                l = [str(s)] + l[3:]
            else:
                return [str(s)]



def calc(n):
    done = False
    while done == False:
        open = 0
        for i in range(0, len(n)):
            if i < len(n):
                # print(i, len(n))
                if n[i] == "(":
                    open = i
                if n[i] == ")":
                    result = sum(n[open+1: i])  # sum has to return as a list
                    n = n[0:open] + result + n[i+1:]
                    break
                if i == len(n) - 1:
                    result = sum(n)
                    done = True
    return int(result[0])


total = 0
for line in input:
    total = total + calc(line)
print(total)
