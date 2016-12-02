from maps import Direction, Location


with open('input.txt') as f:
    instructions = f.read().strip().split(', ')

# start at 0,0 facing North
start = Location(0, 0)
direction = Direction.NORTH

current = start
for inst in instructions:
    lr = inst[0]
    n = int(inst[1:])

    # turn left or right
    if lr == 'L':
        direction = Direction.rotate_left(direction)
    elif lr == 'R':
        direction = Direction.rotate_right(direction)

    # walk n units forward
    current = current.add(direction, n)

# report the distance back to the beginning
print start.distance_to_loc(current)
