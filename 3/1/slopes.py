# Open file, get a number for lines and width of the text
file1 = open("input.txt")
slopes = file1.read().splitlines()
hills = len(slopes)
width = len(slopes[0])
# Set start position. Line and column.
l = 0
c = 0
trees = 0

while l < hills-1:
    c += 3
    l += 1
    if c > width-1:
        c = (c - width)
    if slopes[l][c] == '#':
        trees += 1
print(trees) 
