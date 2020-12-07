file1 = open("input.txt")
start_passports = file1.read().split("\n\n")
passports = []
for i in start_passports:
    pass_string = i.replace('\n', ' ')
    passports.append(pass_string)

fields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
#optional = "cid"
full_matches = 0
without_cid = 0
truths = 0
haircolors = "0123456789abcdef"
eyecolors = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]

def byr(birthy):
	if 1920 <= int(birthy) <= 2002:
		return True
def iyr(issuey):
	if 2010 <= int(issuey) <= 2020:
		return True
def eyr(expy):
	if 2020 <= int(expy) <= 2030:
		return True
def hgt(height):
	if height[-2:] == 'cm':
		if len(height) == 5:
			if 150 <= int(height[0:3]) <= 193:
				return True
	if height[-2:] == 'in':
		if len(height) == 4:
			if 59 <= int(height[0:2]) <= 76:
				return True
def hcl(hairc):
	if len(hairc) == 7:
		for i in hairc[1:]:
			if i not in haircolors:
				return False
		if hairc[0] != '#':
			return False
		return True
def ecl(eyec):
	if eyec not in eyecolors:
		return False
	return True
def pid(dob):
	if len(dob) == 9:
		if str.isdigit(dob):
			return True
def cid(countryid):
	return False

for i in passports:
	if all(x in i for x in fields):
		truths = 0
		verification = i.split(' ')
		length=len(verification)
		for y in verification:
			if y:
				if locals()[(y[0:3])](y[4:]) is True:
					truths += 1
		if truths == 7:
			without_cid += 1
print(without_cid)
