import enum

import weapon
import body


class Team(enum.Enum):
    BLUE = 0
    RED = 1


class Robot:
    hp: int


class ActivatedRobot(Robot):

    def __init__(self, team: Team):
        self.team = team
        self.bodies: List[body.Body] = [body.SimpleBody(), ]
        self.weapons: List[weapon.Weapon] = [weapon.BasicShot(), ]
        self.hp: int = 2
        self.movement: int = 1
        self.weapon_slots: int = 1


class DeactivatedRobot(Robot):

    def __init__(self):
        self.hp = 1
