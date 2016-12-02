from maps_part_two import Direction, Location


with open('input.txt') as f:
    instructions = f.readlines()

# start at 0,0 facing North
start = Location(0, 0)
direction = Direction.NORTH

code = []
for instuction_line in instructions:
    current = start
    for i in instuction_line.strip():
        if i == 'U':
            current = current.add(Direction.NORTH)
        elif i == 'R':
            current = current.add(Direction.EAST)
        elif i == 'D':
            current = current.add(Direction.SOUTH)
        elif i == 'L':
            current = current.add(Direction.WEST)
    code.append(current.to_int())

print code