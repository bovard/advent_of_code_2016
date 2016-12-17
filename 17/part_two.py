
import hashlib

OPEN = ['b', 'c', 'd', 'e', 'f']

# mine
PASSCODE = 'dmypynyp'


states = [("", (0, 0))]
while len(states) > 0:
    entry = states[0]
    states = states[1:]
    path_so_far = entry[0]
    point = entry[1]
    if min(point) < 0 or max(point) > 3:
        continue

    if point[0] == 3 and point[1] == 3:
        if len(path_so_far) > len(longest_path):
            print len(path_so_far), len(states)
            longest_path = path_so_far
        continue

    m = hashlib.md5()
    to_hash = "{}{}".format(PASSCODE, path_so_far)
    m.update(to_hash)
    anser = m.hexdigest()

    if anser[0] in OPEN and point[1] > 0:
        states.append((path_so_far + 'U', (point[0], point[1] - 1)))
    if anser[1] in OPEN and point[1] < 3:
        states.append((path_so_far + 'D', (point[0], point[1] + 1)))
    if anser[2] in OPEN and point[0] > 0:
        states.append((path_so_far + 'L', (point[0] - 1, point[1])))
    if anser[3] in OPEN and point[0] < 3:
        states.append((path_so_far + 'R', (point[0] + 1, point[1])))


print longest_path
print len(longest_path)
