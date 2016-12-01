from maps import Direction, Location


with open('input.txt') as f:
    instructions = f.read().strip().split(', ')

start = Location(0, 0)
current = start
direction = Direction.NORTH

visited = [start]
i = 0
for inst in instructions:
    i += 1
    lr = inst[0]
    n = int(inst[1:])
    if lr == 'L':
        direction = Direction.rotate_left(direction)
    elif lr == 'R':
        direction = Direction.rotate_right(direction)
    for i in range(n):
        current = current.add(direction, 1)
        if current in visited:
            print start.distance_to_loc(current)
            exit(0)
        else:
            visited.append(current)
