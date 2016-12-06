
with open('input.txt') as f:
    instructions = f.readlines()

count_dicts = [{}, {}, {}, {}, {}, {}, {}, {}, {}]

for line in instructions:
    chars = line.split('[')[0]
    for i in range(len(chars)):
        c = chars[i]
        if not count_dicts[i].get(c):
            count_dicts[i][c] = 1
        else:
            count_dicts[i][c] += 1

result = ''
for dic in count_dicts:
    results = dic.items()
    results.sort(key=lambda x: x[1])
    result += results[0][0]

print result
