from typing import List, Tuple, Optional

from src import body, weapon
from src.base import Team, Direction


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
        self.position: Optional[Tuple[int, int]] = None

    def turn(self, direction: Direction):
        if direction.name == 'NORTH':
            self.facing = [1, 0, 0, 0]
        elif direction.name == 'EAST':
            self.facing = [0, 1, 0, 0]
        elif direction.name == 'SOUTH':
            self.facing = [0, 0, 1, 0]
        elif direction.name == 'WEST':
            self.facing = [0, 0, 0, 1]

    def attack(self, idx: int = 0) -> weapon.Weapon:
        try:
            return self.weapons[idx]
        except IndexError as e:
            print(e)


class DeactivatedRobot(Robot):

    def __init__(self):
        super().__init__()
        self.hp = 1
