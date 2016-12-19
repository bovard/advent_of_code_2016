

number = 3012210



def take(elves):
    i = 0
    while sum(elves) > 1:
        try:
            first = elves[i:].index(1)
            try:
                target = elves[i + first + 1:].index(1)
                elves[i + first + target + 1] = 0
                i = i + first + target + 1
            except ValueError, e:
                target = elves.index(1)
                elves[target] = 0
                i = 0
        except ValueError, e:
            i = 0

    return elves.index(1)

tar = []
for i in range(number):
    tar.append(1)

print take(tar)
