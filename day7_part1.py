def check(input):
    for colour in rule_dict[input]:
        if colour == "shinygold":
            return True
        elif colour == "end":
            break
        elif check(colour) == True:
            return True


f = open('day7_input.txt', 'r')
input=f.readlines()

rule_dict = {}
for rule in input:
    rule = rule.replace(",", "")
    rule = rule.replace("\n", "")
    rule = rule.split(" ")
    if rule[4] == "no":
        rule_dict[rule[0] + rule[1]] = ["end"]
    else:
        for i in range(0, len(rule)):
            if i > 4 and i%4 == 1:
                if rule[0]+rule[1] in rule_dict.keys():
                    (rule_dict[rule[0]+rule[1]]).append(rule[i]+rule[i+1])
                else:
                    rule_dict[rule[0]+rule[1]] = [rule[i]+rule[i+1]]

total = 0
for key in rule_dict:
    for colour in rule_dict[key]:
        if colour == "shinygold":
            total = total + 1
            break
        elif colour == "end":
            break
        else:
            if check(colour) == True:
                total = total + 1
                break

print(total)
