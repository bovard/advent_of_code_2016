
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

    def add(self, direction):
        if direction == Direction.NORTH:
            return Location(self.x, min(self.y + 1, 1))
        elif direction == Direction.EAST:
            return Location(min(self.x + 1, 1), self.y)
        elif direction == Direction.SOUTH:
            return Location(self.x, max(self.y - 1, -1))
        elif direction == Direction.WEST:
            return Location(max(self.x - 1, -1), self.y)

    def distance_to_loc(self, loc):
        return abs(self.x - loc.x) + abs(self.y - loc.y)

    def to_int(self):
        if self.x == -1 and self.y == 1:
            return 1
        if self.x == 0 and self.y == 1:
            return 2
        if self.x == 1 and self.y == 1:
            return 3

        if self.x == -1 and self.y == 0:
            return 4
        if self.x == 0 and self.y == 0:
            return 5
        if self.x == 1 and self.y == 0:
            return 6

        if self.x == -1 and self.y == -1:
            return 7
        if self.x == 0 and self.y == -1:
            return 8
        if self.x == 1 and self.y == -1:
            return 9
