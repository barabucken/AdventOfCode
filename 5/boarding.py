file1 = open("input.txt")
bpass = file1.read().split()
results = []

for i in bpass:
	rows = [0,127]
	columns = [0, 7]
	for x in i[0:7]:
		if x == "F":
			rows[1] = int(((int(rows[0]) + int(rows[1]))/2))
		if x == "B":
			rows[0] = int(rows[1]) - int((((int(rows[1]) - int(rows[0])) - 1) / 2))
	for y in i[7:]:
		if y == "L":
			columns[1] = int(((int(columns[0]) + int(columns[1]))/2))
		if y == "R":
			columns[0] = int(columns[1]) - int((((int(columns[1]) - int(columns[0])) - 1) / 2))
	results.append((rows[0] * 8) + columns[0])
results.sort()

print("Highest result is", results[-1])
print("Lowest result is", results[0])

for z in range(results[0], results[-1]):
	if z not in results:
		print("Missing number is",z)

