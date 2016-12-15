
sizes = [17, 3, 19, 13, 7, 5]
positions = [15, 2, 4, 2, 2, 0]


def simulate(szs, pos):
    for i in range(len(szs)):
        if pos[i] + i + 1 != szs[i]:
            return False
    return True

t = 0
while True:
    if ((15 + t + 1) % 17 == 0 and
        (2 + t + 2) % 3 == 0 and
        (4 + t + 3) % 19 == 0 and
        (2 + t + 4) % 13 == 0 and
        (2 + t + 5) % 7 == 0 and
        (0 + t + 6) % 5 == 0):
        print t
        break
    t += 1


