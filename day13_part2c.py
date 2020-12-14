import numpy
import sys
# print(sys.maxsize)
#
# x = 100000000000000
# print(x + 1000678)

p1 = 19
l1 = [643, 37, 23, 19, 17]
lcm1 = numpy.lcm.reduce(l1)
print(lcm1)

p2 = 50
l2 = [509, 41, 29, 13]
lcm2 = numpy.lcm.reduce(l2)
print(lcm2)

diff = p2-p1

# need x*lm1 - y*lm2 == diff
print(type(lcm1))
print(type(lcm2))

# lcm1 = 176743339
# lcm2 = 7867613

found = False
num = 0

while found == False:
    num = int(num) + int(lcm1)
        # print(count)
    # print(num)
    # print(num, num%lcm2)
    if (num+diff)%lcm2 == 0:
        print((num-19))
        found = True



# found = False
# num = 0
#
# while found == False:
#     num = num + lcm1
#         # print(count)
#     # print(num)
#     # print(num, num%lcm2)
#     if (num+diff)%lcm2 == 0:
#         print((num-19))
#         found = True



#
# found = False
# count = 0
# num = lcm1
#
# while found == False:
#     num = num + lcm1
#     while num > 16000000:
#         num = num - lcm2
#         count = count + 1
#         # print(count)
#     # print(num)
#     # print(num, num%lcm2)
#     if (num+diff)%lcm2 == 0:
#         print((num-19))
#         print(count)
#         found = True







# way 3

# x = 1
# y = 1
#
# found = False
#
# one = 100000000000000000000
# two = 100000000000000000000
#
# while found == False:
#     one = int(x * lcm1)
#     two = int(y * lcm2)
#     # print(one, two)
#     if two <= one:
#         y = y + 1
#     else:
#         if two - one == diff:
#             print(one - 19)
#             found = True
#         else:
#             x = x + 1
