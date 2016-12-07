
with open('input.txt') as f:
    instructions = f.readlines()

does = 0

for line in instructions:
    is_outside = True
    outside = False
    inside = False
    i = 0
    while i < len(line) - 4:
        #print line[i:i+4]
        if line[i+3] == '[':
            i += 4
            is_outside = False
        elif line[i+3] == ']':
            i += 4
            is_outside = True
        else:
            i += 1
            if line[i] == line[i + 3] and line[i + 1] == line[i + 2]:
                if is_outside:
                    outside = True
                else:
                    inside = True
    if outside and not inside:
        does +=1

print does
