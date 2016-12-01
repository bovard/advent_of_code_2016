from maps import Direction, Location


with open('input.txt') as f:
    instructions = f.read().strip().split(', ')

start = Location(0, 0)
current = start
direction = Direction.NORTH

for inst in instructions:
    lr = inst[0]
    n = int(inst[1:])
    if lr == 'L':
        direction = Direction.rotate_left(direction)
    elif lr == 'R':
        direction = Direction.rotate_right(direction)
    current = current.add(direction, n)

print start.distance_to_loc(current)



