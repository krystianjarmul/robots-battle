from typing import List, Tuple

from src.arena import Arena
from src.robot import Robot, ActivatedRobot, DeactivatedRobot
from src.weapon import Weapon
from src.base import Move, Direction, Team, Position
from src.utils import get_turned_matrix, get_shift


class Battle:

    def __init__(self):
        self.arena: Arena = Arena()
        self.red_robot: Robot = ActivatedRobot(Team.RED)
        self.blue_robot: Robot = ActivatedRobot(Team.BLUE)
        self.deactivated_robots: List[Robot] = [
            DeactivatedRobot(i) for i in range(8)
        ]

    def start(self):
        self.arena.init()
        self._init_robots()

    def move(self, robot: ActivatedRobot, move: Move):
        position = robot.position
        dest = self.arena.move(position, move)
        robot.position = dest

    def turn(self, robot: ActivatedRobot, direction: Direction):
        robot.turn(direction)

    def attack(self, robot: ActivatedRobot, idx: int = 0):
        weapon = robot.attack(idx)
        attack_fields = self._get_attack_fields(robot, weapon)

        attacked_positions = [
            field for field in attack_fields
            if self.arena.board[field[0]][field[1]] == 'x'
        ]

        self._subtract_hp(attacked_positions)

    def die(self, robot: Robot):
        if isinstance(robot, DeactivatedRobot):
            self.deactivated_robots.pop(robot.id)

        self.arena.drop_item(robot.position)

    def _init_robots(self):
        self._set_robot(Team.RED)
        self._set_robot(Team.BLUE)
        self._set_deactivated_robots()

    def _get_attack_fields(
            self, robot: ActivatedRobot, weapon: Weapon
    ) -> List[Position]:
        facing_idx = robot.facing.index(1)
        weapon_range = get_turned_matrix(weapon.range, facing_idx)
        weapon_direction = get_turned_matrix(weapon.directions, facing_idx)

        attack_attrs = [
            {
                'x_start': robot.position[0] - 1 + row_idx,
                'y_start': robot.position[1] - 1 + col_idx,
                'range': weapon_range[row_idx][col_idx]
            }
            for row_idx, row in enumerate(weapon_direction)
            for col_idx, col in enumerate(row)
            if col
        ]

        attack_fields = [
            (
                attr['x_start'] + get_shift(robot.facing, i)[0],
                attr['y_start'] + get_shift(robot.facing, i)[1]
            )
            for attr in attack_attrs for i in range(attr['range'])
        ]

        return attack_fields

    def _set_robot(self, team: Team):
        if team.name == 'RED':
            robot_red_position_y = self.arena.board[0].index('x')
            self.red_robot.position = (0, robot_red_position_y)
            self.red_robot.facing = [0, 0, 1, 0]

        elif team.name == 'BLUE':
            robot_blue_position_y = self.arena.board[5].index('x')
            self.blue_robot.position = (5, robot_blue_position_y)

    def _set_deactivated_robots(self):
        battleground = self.arena.board[1:-1]
        robots_position = [
            (row_idx, col_idx)
            for row_idx, row in enumerate(battleground)
            for col_idx, col in enumerate(row)
            if col == 'x'
        ]

        for robot, position in zip(self.deactivated_robots, robots_position):
            robot.position = position

    def _subtract_hp(self, positions: List[Position]):
        all_robots = [*self.deactivated_robots, self.red_robot, self.blue_robot]
        for robot in all_robots:
            if robot.position in positions:
                robot.hp -= 1
