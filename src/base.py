import enum
from typing import Tuple, List

Position = Tuple[int, int]
Matrix = List[List[int]]


class Item:
    position: Position
    picked: bool = False


class Move(enum.Enum):
    UP = 0
    RIGHT = 1
    DOWN = 2
    LEFT = 3


class Team(enum.Enum):
    BLUE = 0
    RED = 1


class Direction(enum.Enum):
    NORTH = 0
    EAST = 1
    SOUTH = 2
    WEST = 3
