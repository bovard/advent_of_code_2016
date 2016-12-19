import math

NUM = 3012210

def solve_elves(circle):
    i = 0
    j = 0
    while(len(circle)) > 1:
        j += 1
        if j % 10000 == 0:
            j = 0
            print len(circle)
        target = i + int(math.floor(len(circle) / 2))
        target %= len(circle)
        circle.pop(target)
        if target > i:
            i += 1
        if i >= len(circle):
            i = 0
    return circle[0]


for i in range(2, 100):
    test = []
    for j in range(1, i + 1):
        test.append(j)
    print i, solve_elves(test)
