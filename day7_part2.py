def check(input):
    temp_count = 0
    for colour in range(0, len(rule_dict[input])):
        if colour == 0:
            temp_count = temp_count + rule_dict[input][0]
        elif rule_dict[input][colour] == "end":
            break
        elif colour > 0 and colour%2 == 0:
            temp_count = temp_count + (rule_dict[input][colour-1] * check(rule_dict[input][colour]))
        else:
            continue
    return temp_count


f = open('day7_input.txt', 'r')
input=f.readlines()

rule_dict = {}
for rule in input:
    rule = rule.replace(",", "")
    rule = rule.replace("\n", "")
    rule = rule.split(" ")
    if rule[4] == "no":
        rule_dict[rule[0] + rule[1]] = [0, "end"]
    else:
        num = 0
        for i in range(0, len(rule)):
            if i > 3 and i%4 == 0:
                num = num + int(rule[i])
        for i in range(0, len(rule)):
            if i > 4 and i%4 == 1:
                if rule[0]+rule[1] in rule_dict.keys():
                    (rule_dict[rule[0]+rule[1]]).append(int(rule[i-1]))
                    (rule_dict[rule[0]+rule[1]]).append(rule[i]+rule[i+1])
                else:
                    rule_dict[rule[0]+rule[1]] = [num, int(rule[i-1]), rule[i]+rule[i+1]]

total = 0

for colour in range(0, len(rule_dict["shinygold"])):
    if colour == 0:
        total = total + rule_dict["shinygold"][0]
    elif rule_dict["shinygold"][colour] == "end":
        break
    elif colour > 0 and colour%2 == 0:
        total = total + (rule_dict["shinygold"][colour-1] * check(rule_dict["shinygold"][colour]))
    else:
        continue

print(total)
