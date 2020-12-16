f = open('day16_input.txt', 'r')
input=f.readlines()

prerule = input[0:20]
preyou = input[22:23]
pretickets = input[25:]

rule = []
for i in prerule:
    i= i.replace("\n", "")
    i = i.replace("-", " ")
    i = i.split(" ")
    # print(i)
    temp = [int(i[-5]), int(i[-4])]
    temp2 = [int(i[-2]), int(i[-1])]
    rule.append(temp)
    rule.append(temp2)
# print(rule)

tickets = []
for i in pretickets:
    i = i.replace("\n", "")
    i = i.split(",")
    tickets.append(i)
# print(tickets)   # does not have ints yet

error_rate = 0

for ticket in tickets:
    for number in ticket:
        for pair in rule:
            if pair[0] <= int(number) and int(number) <= pair[1]:
                break
            if pair == rule[-1]:
                error_rate = error_rate + int(number)

print(error_rate)
