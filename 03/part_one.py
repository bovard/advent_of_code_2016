
with open('input.txt') as f:
    instructions = f.readlines()

# start at 0,0 facing North
count = 0

for instuction_line in instructions:
    line = instuction_line.strip().split(' ')
    line = filter(lambda x: len(x) > 0, line)
    line = [int(l) for l in line]
    line = sorted(line)
    if line[0] + line[1] > line[2]:
        count += 1

print count