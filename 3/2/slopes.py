# Open file, get a number for lines and width of the text
file1 = open("input.txt")
slopes = file1.read().splitlines()
hills = len(slopes)
width = len(slopes[0])
# Set start position. Line and column.
trees = 0
treelist = []
counter = [[1, 1], [3, 1], [5, 1], [7, 1], [1, 2]]
for i in counter:
    print(i[0], i[1])
    c = 0
    l = 0
    while l < hills-1:
        c += i[0]
        l += i[1]
        if c > width-1:
            c = (c - width)
        if slopes[l][c] == '#':
            trees += 1
    print(trees)
    treelist.append(trees)
    trees = 0
    
result = 1
for r in treelist:
    result = result * r
    print(result)
