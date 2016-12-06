
with open('input.txt') as f:
    instructions = f.readlines()

# start at 0,0 facing North
count = 0
real = 0

for line in instructions:
    chars = line.split('[')[0]
    chk = line.split('[')[1][:-1]
    letters = {}
    for c in chars:
        if c.isalpha():
            if not letters.get(c):
                letters[c] = 1
            else:
                letters[c] += 1
    results = letters.items()
    results.sort(key=lambda x: x[0])
    results.sort(key=lambda x: x[1], reverse=True)
    valid = True
    for i in range(5):
        print chk[i], results[i][0]
        if len(results) < 5 or not chk[i] == results[i][0]:
            valid = False
    if valid:
        count += 1
        print line[-3 + line.index('['):line.index('[')]
        i_d = int(line[-3 + line.index('['):line.index('[')])
        real += i_d


print count
print real