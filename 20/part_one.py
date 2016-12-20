
with open('input.txt') as f:
    instructions = f.readlines()
    instructions = [(int(i.split('-')[0]), int(i.split('-')[1])) for i in instructions]

lowest = 0

done = False
i = 0
while not done and i < 20:
    i += 1
    #print lowest
    touched = False
    for line in instructions:
        if line[0] <= lowest and lowest <= line[1]:
            #print line, lowest
            touched = True
            lowest = line[1] + 1
    if not touched:
        done = True
        print lowest

