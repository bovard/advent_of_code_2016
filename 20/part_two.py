
with open('input.txt') as f:
    instructions = f.readlines()
    instructions = [(int(i.split('-')[0]), int(i.split('-')[1])) for i in instructions]

lowest = 0

free = 0
i = 0
while i <= 4294967295:
    if i % 1000000 == 0:
        print i, 4294967295
    add = True
    for line in instructions:
        if line[0] <= i and i <= line[1]:
            add = False
            i = line[1] + 1
            break
    if add:
        i += 1
        free += 1

print free



