import random
from typing import List

from src.arena import Arena
from src.robot import Robot, ActivatedRobot, DeactivatedRobot
from src.base import Move, Direction, Team, Position
from src.utils import get_turned_matrix, get_shift, is_field_correct, \
    validate_fields
from src.config import logger
from src import weapon
from src import body
from src.weapon import Weapon, Sword

ITEMS = (
    weapon.Sword,
    weapon.Laser,
    weapon.Explosion,
    weapon.DualLaser,
    body.BattleBody,
    body.HardBody,
    body.LightBody,
)


# TODO ROUNDS -> MOVE, TURN, ATTACK, SELECT WEAPON


class Battle:

    def __init__(self):
        self.arena: Arena = Arena()
        self.red_robot: Robot = ActivatedRobot(Team.RED)
        self.blue_robot: Robot = ActivatedRobot(Team.BLUE)
        self.deactivated_robots: List[Robot] = [
            DeactivatedRobot() for _ in range(8)
        ]
        self.items: List[Item] = []
        self.has_moved = False

    def start(self):
        self.arena.init()
        self._init_robots()
        logger.info('The battle has been started.')

    def move(self, team: Team, move: Move):
        if team == Team.RED:
            robot = self.red_robot
        else:
            robot = self.blue_robot

        position = robot.position
        can_move, is_item = self.arena.move(position, move)
        if can_move:
            robot.move(move)
            self.has_moved = True

        if is_item:
            self.pick_item(team)

    def turn(self, team: Team, direction: Direction, log=True):
        if team == Team.RED:
            robot = self.red_robot
        else:
            robot = self.blue_robot

        robot.turn(direction, log)

    def attack(self, team: Team, extra=False):
        if team == Team.RED:
            robot = self.red_robot
        else:
            robot = self.blue_robot

        weapon = robot.attack(extra)
        attack_fields = self.get_attack_fields(team, extra)

        attacked_positions = [
            field for field in attack_fields
            if self.arena.board[field[0]][field[1]] == 'x'
        ]

        self._subtract_hp(attacked_positions, weapon)
        logger.info(
            'Robot %s has used %s.',
            robot.team.name,
            robot.selected_weapon.name if not extra else robot.extra_weapon.name
        )

    def destroy(self, robot: Robot):
        if isinstance(robot, DeactivatedRobot):
            self.deactivated_robots.pop(self.deactivated_robots.index(robot))
            self.drop_item(robot.position)
            logger.info('Deactivated robot has been destroyed.')

        else:
            if robot.team.name == 'RED':
                self.red_robot = None

            else:
                self.blue_robot = None

            self.arena.board[robot.position[0]][robot.position[1]] = 0
            logger.info('%s robot has been destroyed.', robot.team.name)

    def drop_item(self, position: Position):
        self.arena.drop_item(position)
        item = random.choice(ITEMS)()
        item.position = position
        self.items.append(item)

    def pick_item(self, team: Team):
        if team == Team.RED:
            robot = self.red_robot
        else:
            robot = self.blue_robot

        try:
            item = next(
                item for item in self.items if item.position == robot.position
            )
            robot.pick(item)

            self.items.remove(item)
            logger.info(
                'Robot %s has picked up %s.',
                robot.team.name,
                item.name
            )

        except StopIteration:
            return

    def select_weapon(self, team: Team, idx: int):
        if team == Team.RED:
            robot = self.red_robot
        else:
            robot = self.blue_robot

        robot.select_weapon(idx)

    def select_body(self, team: Team, idx: int):
        if team == Team.RED:
            robot = self.red_robot
        else:
            robot = self.blue_robot

        robot.select_body(idx)

    def select_extra_weapon(self, team: Team, idx: int):
        if team == Team.RED:
            robot = self.red_robot
        else:
            robot = self.blue_robot

        robot.select_extra_weapon(idx)

    def get_attack_fields(
            self, team: Team, extra=False
    ) -> List[Position]:
        if team == Team.RED:
            robot = self.red_robot
        else:
            robot = self.blue_robot

        weapon = robot.attack(extra)
        facing_idx = robot.facing.index(1)
        weapon_range = get_turned_matrix(weapon.range, facing_idx)
        weapon_direction = get_turned_matrix(weapon.directions, facing_idx)

        attack_attrs = [
            {
                'x_start': robot.position[0] - 1 + row_idx,
                'y_start': robot.position[1] - 1 + col_idx,
                'range': weapon_range[row_idx][col_idx],
                'direction': self._get_attack_direction(team, row_idx, col_idx)
            }
            for row_idx, row in enumerate(weapon_direction)
            for col_idx, col in enumerate(row)
            if col
        ]

        attack_fields = [
            (
                attr['x_start'] + get_shift(robot.facing, i, attr['direction'])[
                    0],
                attr['y_start'] + get_shift(robot.facing, i, attr['direction'])[
                    1]
            )
            for attr in attack_attrs for i in range(attr['range'])
        ]

        return validate_fields(attack_fields)

    def _get_attack_direction(
            self, team: Team, row_idx: int, col_idx: int
    ) -> Direction:
        if team == Team.RED:
            robot = self.red_robot
        else:
            robot = self.blue_robot

        y_attack_start = robot.position[0] - 1 + row_idx
        x_attack_start = robot.position[1] - 1 + col_idx
        facing_idx = robot.facing.index(1)
        if facing_idx % 2:
            if x_attack_start == robot.position[1]:
                if y_attack_start < robot.position[0]:
                    return Direction.WEST

                else:
                    return Direction.EAST

        else:
            if y_attack_start == robot.position[0]:
                if x_attack_start < robot.position[1]:
                    return Direction.WEST

                else:
                    return Direction.EAST

        return Direction.NORTH

    def _init_robots(self):
        self._set_robot(Team.RED)
        self._set_robot(Team.BLUE)
        self._set_deactivated_robots()

    def _set_robot(self, team: Team):
        if team.name == 'RED':
            robot_red_position_y = self.arena.board[0].index('x')
            self.red_robot.position = (0, robot_red_position_y)
            self.red_robot.facing = [0, 0, 1, 0]

        elif team.name == 'BLUE':
            robot_blue_position_y = self.arena.board[5].index('x')
            self.blue_robot.position = (5, robot_blue_position_y)

    def _set_deactivated_robots(self):
        robots_position = [
            (row_idx, col_idx)
            for row_idx, row in enumerate(self.arena.board)
            for col_idx, col in enumerate(row)
            if col == 'x' and row_idx not in [0, 5]
        ]

        for robot, position in zip(self.deactivated_robots, robots_position):
            robot.position = position

    def _subtract_hp(self, positions: List[Position], weapon: Weapon):
        all_robots = [*self.deactivated_robots, self.red_robot, self.blue_robot]
        for robot in all_robots:
            if not robot:
                continue

            if robot.position in positions:
                robot.hp -= weapon.attack
