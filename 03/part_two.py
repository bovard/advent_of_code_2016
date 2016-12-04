
with open('input.txt') as f:
    instructions = f.readlines()

# start at 0,0 facing North
count = 0


def fix_line(line):
    line = line.strip().split(' ')
    line = filter(lambda x: len(x) > 0, line)
    line = [int(l) for l in line]
    return line

for i in range(0, len(instructions), 3):
    first = fix_line(instructions[i])
    second = fix_line(instructions[i+1])
    third = fix_line(instructions[i+2])

    for i in range(3):
        line = [first[i],second[i],third[i]]
        line = sorted(line)
        if line[0] + line[1] > line[2]:
            count += 1

print count