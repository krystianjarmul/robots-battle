import arena
import robot


class Battle:

    def __init__(self):
        self.arena = arena.Arena()
        self.robot_red = robot.ActivatedRobot(robot.Team.RED)
        self.robot_blue = robot.ActivatedRobot(robot.Team.BLUE)

    def start(self):
        self.arena.init()
