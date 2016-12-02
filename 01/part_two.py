from maps import Direction, Location


with open('input.txt') as f:
    instructions = f.read().strip().split(', ')

# start at 0,0 facing north
start = Location(0, 0)
direction = Direction.NORTH

# keep track of our current location, and all locations visited
current = start
visited = [start]
for inst in instructions:
    lr = inst[0]
    n = int(inst[1:])

    # turn left
    if lr == 'L':
        direction = Direction.rotate_left(direction)
    elif lr == 'R':
        direction = Direction.rotate_right(direction)

    # one square at a time walk forward, checking if we cross our old path
    for i in range(n):
        current = current.add(direction, 1)
        if current in visited:
            print start.distance_to_loc(current)
            exit(0)
        else:
            visited.append(current)
