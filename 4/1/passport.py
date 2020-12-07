file1 = open("test.txt")
start_passports = file1.read().split("\n\n")
passports = []
#.split("\n\n")
for i in start_passports:
    pass_string = i.replace('\n', ' ')
    passports.append(pass_string)

fields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
optional = "cid"
full_matches = 0
without_cid = 0

def byr():
	print("Byr found")
def iyr():
	print("Iyr found")
def eyr():
	print("Eyr found")
def hgt():
	print("Hgt found")
def hcl():
	print("Hcl found")
def ecl():
	print("ecl found")
def pid():
	print("pid found")
def cid():
	print("cid found")

options = {	byr : byr,
		iyr : iyr,
		eyr : eyr,
		hgt : hgt,
		hcl : hcl,
		ecl : ecl,
		pid : pid,
		cid : cid
}

#print(passports)
#print(type(passports))
for i in passports:
#    print(passports[i])
    if all(x in i for x in fields):
#        print(i)
        verification = i.split(' ')
        print(verification)
        length=len(verification)
        print(length)
        for y in verification:
            print(y[0:3])
            locals()[(y[0:3])]()


        without_cid += 1
print(without_cid)
