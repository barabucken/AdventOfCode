file1 = open("input.txt")
start_passports = file1.read().split("\n\n")
passports = []

for i in start_passports:
    pass_string = i.replace('\n', ' ')
    passports.append(pass_string)

fields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
optional = "cid"
full_matches = 0
without_cid = 0

for i in passports:

    if all(x in i for x in fields):
        without_cid += 1
print(without_cid)
