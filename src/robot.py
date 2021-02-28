from typing import List, Optional

from src.body import Body, SimpleBody
from src.weapon import Weapon, BasicShot
from src.base import Team, Direction, Position


class Robot:

    def __init__(self):
        self.hp: int
        self.position: Optional[Position] = None

    def is_alive(self) -> bool:
        return bool(self.hp)


class ActivatedRobot(Robot):

    def __init__(self, team: Team):
        super().__init__()
        self.team = team
        self.hp = 2
        self.bodies: List[Body] = [SimpleBody(), ]
        self.weapons: List[Weapon] = [BasicShot(), ]
        self.movement: int = 1
        self.weapon_slots: int = 1
        self.facing: List[int] = [1, 0, 0, 0]
        self.selected_weapon = self.weapons[0]

    def turn(self, direction: Direction):
        if direction.name == 'NORTH':
            self.facing = [1, 0, 0, 0]
        elif direction.name == 'EAST':
            self.facing = [0, 1, 0, 0]
        elif direction.name == 'SOUTH':
            self.facing = [0, 0, 1, 0]
        elif direction.name == 'WEST':
            self.facing = [0, 0, 0, 1]

    def attack(self) -> Weapon:
        try:
            return self.selected_weapon
        except IndexError as e:
            print(e)

    def select_weapon(self, idx: int):
        try:
            self.selected_weapon = self.weapons[idx]
        except IndexError as e:
            print(e)


class DeactivatedRobot(Robot):

    def __init__(self):
        super().__init__()
        self.hp = 1
