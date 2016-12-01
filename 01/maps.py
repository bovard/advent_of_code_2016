
class Direction:
    # never eat sour wheat
    NORTH = 0
    EAST = 1
    SOUTH = 2
    WEST = 3

    @staticmethod
    def rotate_left(direction):
        if direction == Direction.NORTH:
            return Direction.WEST
        elif direction == Direction.WEST:
            return Direction.SOUTH
        elif direction == Direction.SOUTH:
            return Direction.EAST
        elif direction == Direction.EAST:
            return Direction.NORTH

    @staticmethod
    def rotate_right(direction):
        if direction == Direction.NORTH:
            return Direction.EAST
        elif direction == Direction.EAST:
            return Direction.SOUTH
        elif direction == Direction.SOUTH:
            return Direction.WEST
        elif direction == Direction.WEST:
            return Direction.NORTH


class Location:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, loc):
        return self.x == loc.x and self.y == loc.y

    def add(self, direction, n):
        if direction == Direction.NORTH:
            return Location(self.x, self.y + n)
        elif direction == Direction.EAST:
            return Location(self.x + n, self.y)
        elif direction == Direction.SOUTH:
            return Location(self.x, self.y - n)
        elif direction == Direction.WEST:
            return Location(self.x - n, self.y)

    def distance_to_loc(self, loc):
        return abs(self.x - loc.x) + abs(self.y - loc.y)