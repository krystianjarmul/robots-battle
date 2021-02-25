from unittest import mock

from src.battle import Battle
from src.arena import Arena
from src.robot import ActivatedRobot
from src.base import Move, Direction
from src.utils import turn_matrix


def get_robot(battle, pos, facing=[1, 0, 0, 0], blue=False):
    battle.arena.board[pos[0]][pos[1]] = 'x'
    if blue:
        robot = battle.robot_red
    else:
        robot = battle.robot_blue
    robot.position = (pos[0], pos[1])
    robot.facing = facing
    return robot


def test_default_attributes():
    battle = Battle()
    assert isinstance(battle.arena, Arena)
    assert isinstance(battle.robot_red, ActivatedRobot)
    assert isinstance(battle.robot_blue, ActivatedRobot)


@mock.patch('src.arena.Arena.init')
@mock.patch('src.battle.Battle.init_robots')
def test_battle_start(init_robots_mock, init_mock):
    battle = Battle()

    battle.start()

    assert init_mock.called
    assert init_robots_mock.called


def test_move_the_robot():
    battle = Battle()
    battle.robot_red.position = (2, 3)
    battle.arena.board[2][3] = 'x'
    robot = battle.robot_red

    battle.move(robot, Move.UP)

    assert battle.arena.board[2][3] == 0
    assert battle.arena.board[1][3] == 'x'


def test_robots_initialize():
    battle = Battle()
    battle.start()

    battle.init_robots()

    assert battle.robot_red.position[0] == 0
    assert battle.robot_blue.position[0] == 5


def test_turn_the_robot():
    battle = Battle()
    robot = battle.robot_blue

    battle.turn(robot, Direction.EAST)

    assert battle.robot_blue.facing == [0, 0, 0, 1]


def test_red_robot_looks_south_by_default():
    battle = Battle()
    battle.start()

    assert battle.robot_red.facing == [0, 0, 1, 0]


# def test_attack_check_if_any_robot_in_range():
#     battle = Battle()
#     red_robot = get_robot(battle, (3, 3))
#     blue_robot = get_robot(battle, (2, 3), blue=True)
#
#     battle.attack(red_robot)
#     assert blue_robot.hp == 1
#
#
# def test_attack_check_if_any_robot_not_in_range():
#     battle = Battle()
#     red_robot = get_robot(battle, (3, 3))
#     blue_robot = get_robot(battle, (2, 4), blue=True)
#     battle.attack(red_robot)
#     assert blue_robot.hp == 2

def test_turn_matrix_once():
    X = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]

    X_turned = turn_matrix(X)

    assert X_turned == [
        [7, 4, 1],
        [8, 5, 2],
        [9, 6, 3]
    ]


def test_turn_matrix_couple_times():
    X = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]

    X_turned = turn_matrix(X, 2)

    assert X_turned == [
        [9, 8, 7],
        [6, 5, 4],
        [3, 2, 1]
    ]
