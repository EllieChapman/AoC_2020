f = open('day1_part1.txt', 'r')
d=f.read()

d = d.replace("\n", " ")
pre_nums = d.split(" ")

nums = []

for num in pre_nums:
    nums.append(int(num))

# for num in nums:
#     print(num)

# ###### For part 1
# for ii in range(0, len(nums)-1):
#     for jj in range(ii+1, len(nums)):
#         # print(nums[ii], nums[jj])
#         if int(nums[ii]) + int(nums[jj]) == 2020:
#             print(int(nums[ii]) * int(nums[jj]))

###### For part 2
for ii in range(0, len(nums)-2):
    for jj in range(ii+1, len(nums)-1):
        for kk in range(jj+1, len(nums)):
            if nums[ii] + nums[jj] + nums[kk] == 2020:
                print(nums[ii] * nums[jj] * nums[kk])
                break
