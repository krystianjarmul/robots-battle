from typing import List, Optional

from src.body import Body, SimpleBody
from src.weapon import Weapon, BasicShot, DualLaser, Laser
from src.base import Team, Direction, Position, Item
from src.config import logger


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
        return self.selected_weapon

    def pick(self, item: Item):
        if isinstance(item, Weapon):
            if item not in self.weapons:
                self.weapons.append(item)

        else:
            if item not in self.bodies:
                self.bodies.append(item)

    def select_weapon(self, idx: int):
        try:
            if self.selected_weapon != self.weapons[idx]:
                self.selected_weapon = self.weapons[idx]
                logger.info(
                    'Robot %s has selected %s.',
                    self.team.name,
                    self.selected_weapon.name
                )
            else:
                logger.info(
                    '%s is already selected by Robot %s.',
                    self.selected_weapon.name,
                    self.team.name
                )

        except IndexError as e:
            logger.error('Cannot select weapon from slot %s.', idx)


class DeactivatedRobot(Robot):

    def __init__(self):
        super().__init__()
        self.hp = 1
