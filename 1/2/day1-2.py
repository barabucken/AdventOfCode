import numpy as np

lines = np.loadtxt("1.txt", delimiter="\n", dtype ='int')

target = 2020

sum = 0
test1 = 0
test2 = 0
test3 = 0

first = 0
second = 1
third = 2

while sum != target:
    sum = lines[first] + lines[second] + lines[third]
    if sum == target:
        test1 = lines[first]
        test2 = lines[second]
        test3 = lines[third]
        print(test1*test2*test3)
        print("And there it is")
        exit()
    else:
        third += 1
    if third == len(lines):
        second += 1
        third = second+1
    if second == len(lines)-1:
        first += 1
        second = first+1
        third = second+1
