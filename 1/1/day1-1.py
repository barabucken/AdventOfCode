import numpy as np

lines = np.loadtxt("1.txt", delimiter="\n", dtype ='int')

target = 2020
sum = 0
start = 0
test1 = 0
test2 = 0
increment = 0

while sum != target:
    sum = lines[0+increment] + lines[1+start]
    if sum == target:
        print(sum)
        test1 = lines[0+increment]
        test2 = lines[0+start+1]
        print(start, increment)
        print(test1, test2)
        print(test1*test2)
    else:
        start += 1
    if len(lines) == start+1:
        increment +=1
        start = increment
