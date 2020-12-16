f = open('day16_input.txt', 'r')
input=f.readlines()

prerule = input[0:20]
preme = input[22:23]
pretickets = input[25:]

me = preme[0].replace("\n", "").split(",")

rule = []
for i in prerule:
    i= i.replace("\n", "")
    i = i.replace("-", " ")
    i = i.split(" ")
    temp = [[int(i[-5]), int(i[-4])], [int(i[-2]), int(i[-1])]]
    rule.append(temp)

tickets = []
for i in pretickets:
    i = i.replace("\n", "")
    i = i.split(",")
    tickets.append(i)

## remove incorrect tickets
to_del = []
for ticket in range(0, len(tickets)):
    for number in (tickets[ticket]):
        for pair in rule:
            if (pair[0][0] <= int(number) and int(number) <= pair[0][1]) or (pair[1][0] <= int(number) and int(number) <= pair[1][1]):
                break
            if pair == rule[-1]:
                to_del = [ticket] + to_del
for i in to_del:
    del tickets[i]

dict = {}  # key = position in ticket, value = set of rules satisfied by this position in all tickets checked so far

## Get dict of position in tickets to satisfied rules
for ticket in tickets:
    for i in range(0, len(ticket)):
        sat = [] # list of rule satifyed by number in ticket
        for j in range(0, len(rule)):
            if (rule[j][0][0] <= int(ticket[i]) and int(ticket[i]) <= rule[j][0][1]) or (rule[j][1][0] <= int(ticket[i]) and int(ticket[i]) <= rule[j][1][1]):
                sat.append(j)
        sat_s = set(sat)

        if i in dict:
            dict[i] = dict[i].intersection(sat_s)
        else:
            dict[i] = sat_s

final_dict = {}

for i in range(0, len(rule)):
    for key in dict:
        if len(dict[key]) == 1:
            lone = list(dict[key])
            final_dict[key] = lone[0]
            todel = key
    del dict[todel]

    for key2 in dict:
        dict[key2].remove(lone[0])


want = [0,1,2,3,4,5]
to_check = []

for key4 in final_dict:
    if final_dict[key4] in want:
        to_check.append(key4)

total = 1
for pos in to_check:
    total = total * int(me[pos])
print(total)
