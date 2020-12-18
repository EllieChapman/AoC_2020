f = open('day18_input.txt', 'r')
preinput=f.readlines()

input = []
for i in preinput:
    j = i.replace("(", "( ").replace(")", " )").replace("\n", "")
    k = j.split(" ")
    input.append(k)

def sum(l):
    i = 1
    while "+" in l:
        if l[i] == "+":
            s = int(l[i-1]) + int(l[i+1])
            if i >= 3:
                l = l[0:i-1] + [str(s)] + l[i+2:]
            else:
                l = [str(s)] + l[i+2:]
        else:
            i = i + 2

    i = 1
    while "*" in l:
        i = 1
        if l[i] == "*":
            s = int(l[i-1]) * int(l[i+1])
            if i >= 3:
                l = l[0:i-1] + [str(s)] + l[i+2:]
            else:
                l = [str(s)] + l[i+2:]
        else:
            i = i + 2
    return [l[0]]



def calc(n):
    done = False
    while done == False:
        open = 0
        for i in range(0, len(n)):
            if i < len(n):
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
