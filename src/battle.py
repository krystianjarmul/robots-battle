from typing import List, Tuple

from src.arena import Arena
from src.robot import ActivatedRobot
from src.weapon import Weapon
from src.base import Move, Direction, Team
from src.utils import get_turned_matrix, get_shift


class Battle:

    def __init__(self):
        self.arena = Arena()
        self.robot_red = ActivatedRobot(Team.RED)
        self.robot_blue = ActivatedRobot(Team.BLUE)

    def start(self):
        self.arena.init()
        self.init_robots()

    def move(self, robot: ActivatedRobot, move: Move):
        position = robot.position
        dest = self.arena.move(position, move)
        robot.position = dest

    def turn(self, robot: ActivatedRobot, direction: Direction):
        robot.turn(direction)

    def attack(self, robot: ActivatedRobot, idx: int = 0):
        # szuka czy w zasiegu razenia jest jakis robot
        weapon = robot.attack(idx)
        attack_fields = self.get_attack_fields(robot, weapon)

        # jesli tak - pobiera jego polozenie i sprawdza po wszystkich robotach ktory to
        # jesli nie - nic sie nie dzieje
        # nastepnie odejmuje mu 1hp

    def init_robots(self):
        robot_red_position_y = self.arena.board[0].index('x')
        robot_blue_position_y = self.arena.board[5].index('x')
        self.robot_red.position = (0, robot_red_position_y)
        self.robot_red.facing = [0, 0, 1, 0]
        self.robot_blue.position = (5, robot_blue_position_y)

    def get_attack_fields(
            self, robot: ActivatedRobot, weapon: Weapon
    ) -> List[Tuple[int]]:
        facing_idx = robot.facing.index(1)
        weapon_range = get_turned_matrix(weapon.range, facing_idx)
        weapon_drc = get_turned_matrix(weapon.directions, facing_idx)

        attack_attrs = [
            {
                'x_start': robot.position[0] - 1 + weapon_drc.index(row),
                'y_start': robot.position[1] - 1 + row.index(col),
                'range': weapon_range[weapon_drc.index(row)][row.index(col)]
            }
            for row in weapon_drc for col in row if col
        ]

        attack_fields = [
            (
                attr['x_start'] + get_shift(robot.facing, i)[0],
                attr['y_start'] + get_shift(robot.facing, i)[1]
            )
            for attr in attack_attrs for i in range(attr['range'])
        ]

        return attack_fields
