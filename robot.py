import enum

import weapon
import body


class Team(enum.Enum):
    BLUE = 0
    RED = 1


class Direction(enum.Enum):
    NORTH = 0
    EAST = 1
    SOUTH = 2
    WEST = 3


class Robot:

    def __init__(self):
        self.hp: int
        self.is_alive: bool = True

    def die(self):
        self.is_alive = False


class ActivatedRobot(Robot):

    def __init__(self, team: Team):
        super().__init__()
        self.team = team
        self.hp = 2
        self.bodies: List[body.Body] = [body.SimpleBody(), ]
        self.weapons: List[weapon.Weapon] = [weapon.BasicShot(), ]
        self.movement: int = 1
        self.weapon_slots: int = 1
        self.facing: List[int] = [1, 0, 0, 0]

    def turn(self, direction: Direction):
        if direction.name == 'EAST':
            self.facing = [0, 1, 0, 0]
        elif direction.name == 'SOUTH':
            self.facing = [0, 0, 1, 0]


class DeactivatedRobot(Robot):

    def __init__(self):
        super().__init__()
        self.hp = 1
