from typing import List, Optional

from src.body import Body, SimpleBody, BattleBody
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
        self.bodies: List[Body] = [SimpleBody(), ]
        self.weapons: List[Weapon] = [BasicShot(), ]
        self.movement: int = 1
        self.hp = 2
        self.weapon_slots: int = 1
        self.facing: List[int] = [1, 0, 0, 0]
        self.selected_weapon: Weapon = self.weapons[0]
        self.selected_body: Body = self.bodies[0]
        self.extra_slot: bool = False
        self.extra_weapon: Optional[Weapon] = None

    def turn(self, direction: Direction):
        if direction.name == 'NORTH':
            self.facing = [1, 0, 0, 0]

        elif direction.name == 'EAST':
            self.facing = [0, 1, 0, 0]

        elif direction.name == 'SOUTH':
            self.facing = [0, 0, 1, 0]

        elif direction.name == 'WEST':
            self.facing = [0, 0, 0, 1]

    def attack(self, extra=False) -> Weapon:
        if extra:
            return self.extra_weapon

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

        except IndexError:
            logger.error('This slot is not available.')

    def select_body(self, idx: int):
        try:
            if self.selected_body != self.bodies[idx]:
                self.selected_body = self.bodies[idx]
                self.hp = self.selected_body.hp
                if hasattr(self.selected_body, 'movement'):
                    self.movement = self.selected_body.movement

                if hasattr(self.selected_body, 'extra_slot'):
                    self.extra_slot = self.selected_body.extra_slot

                else:
                    self.extra_slot = False

                logger.info(
                    'Robot %s has selected %s.',
                    self.team.name,
                    self.selected_body.name
                )
            else:
                logger.info(
                    '%s is already selected by Robot %s.',
                    self.selected_body.name,
                    self.team.name
                )

        except IndexError:
            logger.error('This slot is not available.')

    def select_extra_weapon(self, idx: int):
        if not self.extra_slot:
            return

        try:
            if self.weapons[idx] not in [
                self.extra_weapon,
                self.selected_weapon
            ]:
                self.extra_weapon = self.weapons[idx]
                logger.info(
                    'Robot %s has selected extra %s.',
                    self.team.name,
                    self.extra_weapon.name
                )

            else:
                logger.info(
                    '%s is already selected by Robot %s.',
                    self.selected_body.name,
                    self.team.name
                )

        except IndexError:
            logger.error('This slot is not available.')


class DeactivatedRobot(Robot):

    def __init__(self):
        super().__init__()
        self.hp = 1
