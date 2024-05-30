from enum import Enum

NORTH = "North"
EAST = "East"
WEST = "West"
SOUTH = "South"

"""
def move(x, y, direction):
    match direction:
        case NORTH:
            return x, y + 1
        case SOUTH:
            return x, y - 1
        case EAST:
            return x + 1, y
        case WEST:
            return x - 1, y
        case _:
            raise ValueError("Invalid direction")
"""


class Direction(Enum):
    NORTH = "North"
    EAST = "East"
    WEST = "West"
    SOUTH = "South"


def move(x, y, direction):
    match direction:
        case Direction.NORTH:
            return x, y + 1
        case Direction.SOUTH:
            return x, y - 1
        case Direction.EAST:
            return x + 1, y
        case Direction.WEST:
            return x - 1, y
        case _:
            raise ValueError("Invalid direction")