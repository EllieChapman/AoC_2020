import math

f = open('day13_input.txt', 'r')
preinput=f.readlines()

depart = int(preinput[0])

buses = preinput[1].replace(",x", "").split(",")

print(depart)
print(buses)

diff = 0
closest = 0

for i in buses:
    factor = math.trunc(depart/int(i))
    earliest = int(i) * (factor+1)
    if diff != 0:
        if (earliest - depart) < diff:
            diff = earliest - depart
            closest = int(i)
    else:
        diff = earliest - depart
        closest = int(i)

print(diff * closest)
