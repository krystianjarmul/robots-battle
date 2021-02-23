from unittest import mock

from battle import Battle
from arena import Arena
from robot import ActivatedRobot
from base import Move, Team, Direction


def test_default_attributes():
    battle = Battle()
    assert isinstance(battle.arena, Arena)
    assert isinstance(battle.robot_red, ActivatedRobot)
    assert isinstance(battle.robot_blue, ActivatedRobot)


@mock.patch('arena.Arena.init')
@mock.patch('battle.Battle.init_robots')
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

    assert battle.robot_blue.facing == [0, 1, 0, 0]
