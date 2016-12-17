import hashlib

OPEN = ['b', 'c', 'd', 'e', 'f']

PASSCODE = 'dmypynyp'


def path_loc(path):
    x = 0
    y = 0
    for i in range(len(path)):
        if path[i] == 'D':
            y += 1
        elif path[i] == 'U':
            y -= 1
        elif path[i] == 'L':
            x -= 1
        elif path[i] == 'R':
            x += 1
    return x, y



def find_path(passcode, path_so_far):
    point = path_loc(path_so_far)
    if min(point) < 0 or max(point) > 3:
        return None
    if point[0] == 3 and point[1] == 3:
        return path_so_far

    m = hashlib.md5()
    to_hash = "{}{}".format(passcode, path_so_far)
    m.update(to_hash)
    anser = m.hexdigest()


    paths = []
    if anser[0] in OPEN and point[1] > 0:
        paths.append(find_path(passcode, path_so_far + 'U'))
    if anser[1] in OPEN and point[1] < 3:
        paths.append(find_path(passcode, path_so_far + 'D'))
    if anser[2] in OPEN and point[0] > 0:
        paths.append(find_path(passcode, path_so_far + 'L'))
    if anser[3] in OPEN and point[0] < 3:
        paths.append(find_path(passcode, path_so_far + 'R'))

    paths = filter(lambda x: x is not None, paths)

    if len(paths) == 0:
        return None

    shortest = paths[0]
    for p in paths:
        if len(p) < len(shortest):
            shortest = p

    return shortest

anser = find_path(PASSCODE, '')
print anser
