import enum


class Team(enum.Enum):
    BLUE = 0
    RED = 1


class Robot:

    def __init__(self, team: Team):
        self.team = team
