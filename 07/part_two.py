
with open('input.txt') as f:
    instructions = f.readlines()

does = 0

for line in instructions:
    to_match_inside = []
    they_match = False
    is_outside = True
    i = 0
    while i < len(line) - 3:
        #print line[i:i+4]
        if line[i+2] == '[':
            is_outside = False
            i = i + 3
        elif line[i+2] == ']':
            is_outside = True
            i = i + 3
        else:
            if is_outside and line[i] == line[i+2] and line[i] != line[i+1]:
                to_match = "{}{}{}".format(line[i+1], line[i], line[i+1])
                to_match_inside.append(to_match)
            i += 1


    print to_match_inside
    i = 0
    while i < len(line) - 3:
        #print line[i:i+4]
        if line[i+2] == '[':
            i += 3
            is_outside = False
        elif line[i+2] == ']':
            i += 3
            is_outside = True
        else:
            if not is_outside and line[i:i+3] in to_match_inside:
                they_match = True
                print line[i:i+3]
            i += 1

    if they_match:
        does +=1



print does
