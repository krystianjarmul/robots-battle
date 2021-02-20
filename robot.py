import enum

import weapon
import body


class Team(enum.Enum):
    BLUE = 0
    RED = 1


class Robot:

    def __init__(self, team: Team):
        self.team = team
        self.bodies: List[body.Body] = [body.SimpleBody(), ]
        self.weapons: List[weapon.Weapon] = [weapon.BasicShot(), ]
        self.hp = 2
        self.movement = 1
        self.weapon_slots = 1
