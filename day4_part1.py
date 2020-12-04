f = open('day4_input.txt', 'r')
input=f.read()

passports = input.split("\n\n")

new = []
for i in passports:
    new.append(i.replace("\n", " "))

# print(new[0])
# print(new[1])

final = []

for i in new:
    temp = i.split(" ")
    final.append(temp)

# print(final[0][0])

actual = []
for entry in final:
    temp_list = []
    for field in entry:
        temp = field.split(":")
        temp_list.append(temp)
    actual.append(temp_list)



def byr(input):
    if len(input) == 4:
        if 1920 <= int(input) and int(input) <= 2002:
            return True
        else:
            return False
    else:
        return False

def iyr(input):
    if len(input) == 4:
        if 2010 <= int(input) and int(input) <= 2020:
            return True
        else:
            return False
    else:
        return False

def eyr(input):
    if len(input) == 4:
        if 2020 <= int(input) and int(input) <= 2030:
            return True
        else:
            return False
    else:
        return False

def hgt(input):
    if len(input) == 5:
        if input[3:] == "cm":
            if 150 <= int(input[0:3]) and int(input[0:3]) <= 193:
                return True
            else:
                return False
        else:
            return False
    elif len(input) == 4:
        if input[2:] == "in":
            if 59 <= int(input[0:2]) and int(input[0:2]) <= 76:
                return True
            else:
                return False
        else:
            return False
    else:
        return False

def hcl(input):
    num_t = 1
    if len(input) == 7 and input[0] == "#":
        for i in range(1,7):
            if input[i] == "0" or "1" or "2" or "3" or "4" or "5" or "6" or "7" or "8" or "9" or "a" or "b" or "c" or "d" or "e" or "f":
                num_t = num_t * 1
            else:
                num_t = 0
        if num_t == 1:
            return True
        else:
            return False
    else:
        return False

def ecl(input):
    if input == "amb" or "blu" or "brn" or "gry" or "grn" or "hzl" or "oth":
        return True
    else:
        return False

def pid(input):
    tr = 1
    if len(input) == 9:
        for letter in input:
            if letter == "0" or "1" or "2" or "3" or "4" or "5" or "6" or "7" or "8" or "9":
                tr = tr * 1
            else:
                tr = 0
        if tr == 1:
            return True
        else:
            return False
    else:
        return False



total_true = 0
for entry in actual:
    temp_dict = {}
    for field in entry:
        temp_dict[field[0]] = field[1]
    true = 1
    if 'byr' in temp_dict.keys():
        if byr(temp_dict["byr"]):
            true = true * 1
        else:
            true = 0
    else:
        true = 0

    if 'iyr' in temp_dict.keys():
        if iyr(temp_dict["iyr"]):
            true = true * 1
        else:
            true = 0
    else:
        true = 0

    if 'eyr' in temp_dict.keys():
        if eyr(temp_dict["eyr"]):
            true = true * 1
        else:
            true = 0
    else:
        true = 0

    if 'hgt' in temp_dict.keys():
        if hgt(temp_dict["hgt"]):
            true = true * 1
        else:
            true = 0
    else:
        true = 0

    if 'hcl' in temp_dict.keys():
        if hcl(temp_dict["hcl"]):
            true = true * 1
        else:
            true = 0
    else:
        true = 0

    if 'ecl' in temp_dict.keys():
        if ecl(temp_dict["ecl"]):
            true = true * 1
        else:
            true = 0
    else:
        true = 0

    if 'pid' in temp_dict.keys():
        if pid(temp_dict["pid"]):
            true = true * 1
        else:
            true = 0
    else:
        true = 0

    if true == 1:
        total_true = total_true + 1
        print(entry, "\n")

print(total_true)
