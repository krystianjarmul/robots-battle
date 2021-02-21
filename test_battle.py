from unittest import mock

from battle import Battle
from arena import Arena
from robot import ActivatedRobot


def test_default_attributes():
    battle = Battle()
    assert isinstance(battle.arena, Arena)
    assert isinstance(battle.robot_red, ActivatedRobot)
    assert isinstance(battle.robot_blue, ActivatedRobot)


@mock.patch('arena.Arena.init')
def test_battle_start(init_mock):
    battle = Battle()

    battle.start()

    assert init_mock.called
