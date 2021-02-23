from typing import Tuple

import arena
import robot
from base import Move, Direction


class Battle:

    def __init__(self):
        self.arena = arena.Arena()
        self.robot_red = robot.ActivatedRobot(robot.Team.RED)
        self.robot_blue = robot.ActivatedRobot(robot.Team.BLUE)

    def start(self):
        self.arena.init()
        self.init_robots()

    def move(self, robot: robot.ActivatedRobot, move: Move):
        position = robot.position
        self.arena.move(position, move)

    def turn(self, robot: robot.ActivatedRobot, direction: Direction):
        robot.turn(direction)

    def init_robots(self):
        try:
            robot_red_position_y = self.arena.board[0].index('x')
            robot_blue_position_y = self.arena.board[5].index('x')
            self.robot_red.position = (0, robot_red_position_y)
            self.robot_blue.position = (5, robot_blue_position_y)
        except Exception as e:
            print('Arena is not initialized')
