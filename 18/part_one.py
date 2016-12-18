
input = ".^^^.^.^^^^^..^^^..^..^..^^..^.^.^.^^.^^....^.^...^.^^.^^.^^..^^..^.^..^^^.^^...^...^^....^^.^^^^^^^"

TRAP = '^'
SAFE = "."


def get_next(a, b, c):
    if a == TRAP and b == TRAP and not c == TRAP:
        return TRAP
    if not a == TRAP and b == TRAP and c == TRAP:
        return TRAP
    if a == TRAP and not b == TRAP and not c == TRAP:
        return TRAP
    if not a == TRAP and not b == TRAP and c == TRAP:
        return TRAP

    return SAFE

total = len(filter(lambda x: x == SAFE, input))
current = input
for i in range(400000 - 1):
    assert len(current) == len(input)
    next = ""
    for i in range(len(input)):
        if i == 0:
            next += get_next(SAFE, current[i], current[i+1])
        elif i == len(input) - 1:
            next += get_next(current[i-1], current[i], SAFE)
        else:
            next += get_next(current[i-1], current[i], current[i+1])
    current = next
    total += len(filter(lambda x: x == SAFE, current))

print total
