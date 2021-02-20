import enum

import weapon
import body


class Team(enum.Enum):
    BLUE = 0
    RED = 1


class Robot:

    def __init__(self, team: Team):
        self.team = team
        self.body = body.SimpleBody()
        self.weapon = weapon.BasicShot()
        self.hp = self.body.hp
        self.movement = 1
