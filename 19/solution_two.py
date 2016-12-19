
NUM = 3012210
#NUM = 100

i = 2
j = 1
while i <= NUM:
    i += 1
    if j < i/2:
        j += 1
    else:
        j += 2
    print i, j
    if j >= i:
        j = 0