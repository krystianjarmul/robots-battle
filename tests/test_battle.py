import random
from unittest import mock

from src.battle import Battle
from src.arena import Arena
from src.robot import ActivatedRobot, DeactivatedRobot
from src.base import Move, Direction, Team, Item
from src import body
from src import weapon


def get_robot(battle, pos, facing=[1, 0, 0, 0], blue=False, red=False):
    battle.arena.board[pos[0]][pos[1]] = 'x'
    if blue:
        robot = battle.blue_robot
    elif red:
        robot = battle.red_robot
    else:
        robot = battle.deactivated_robots[0]

    robot.position = (pos[0], pos[1])
    robot.facing = facing
    return robot


def test_default_attributes():
    battle = Battle()
    assert isinstance(battle.arena, Arena)
    assert isinstance(battle.red_robot, ActivatedRobot)
    assert isinstance(battle.blue_robot, ActivatedRobot)


@mock.patch('src.arena.Arena.init')
@mock.patch('src.battle.Battle._init_robots')
def test_battle_start(init_robots_mock, init_mock):
    battle = Battle()

    battle.start()

    assert init_mock.called
    assert init_robots_mock.called


def test_move_the_robot():
    battle = Battle()
    battle.red_robot.position = (2, 3)
    battle.arena.board[2][3] = 'x'
    robot = battle.red_robot

    battle.move(robot, Move.UP)

    assert battle.arena.board[2][3] == 0
    assert battle.arena.board[1][3] == 'x'


def test_robots_initialize():
    battle = Battle()
    battle.start()

    battle._init_robots()

    assert battle.red_robot.position[0] == 0
    assert battle.blue_robot.position[0] == 5
    for robot in battle.deactivated_robots:
        assert robot.position is not None


def test_turn_the_robot():
    battle = Battle()
    robot = battle.blue_robot

    battle.turn(robot, Direction.EAST)

    assert battle.blue_robot.facing == [0, 1, 0, 0]


def test_red_robot_looks_south_by_default():
    battle = Battle()
    battle.start()

    assert battle.red_robot.facing == [0, 0, 1, 0]


def test_battle_deactivated_robots_attribute():
    battle = Battle()
    robots = battle.deactivated_robots
    assert len(robots) == 8
    assert any([isinstance(robot, DeactivatedRobot) for robot in robots])


def test_attack_subtract_hp_of_attacked_activated_robot():
    battle = Battle()
    red_robot = get_robot(battle, (3, 3), red=True)
    blue_robot = get_robot(battle, (2, 3), blue=True)

    battle.attack(red_robot)
    assert blue_robot.hp == 1


def test_set_red_robot():
    battle = Battle()
    battle.arena.init()

    battle._set_robot(Team.RED)

    assert battle.red_robot.position[0] == 0


def test_set_blue_robot():
    battle = Battle()
    battle.arena.init()

    battle._set_robot(Team.BLUE)

    assert battle.blue_robot.position[0] == 5


def test_set_deactivated_robots():
    battle = Battle()
    battle.arena.init()

    battle._set_deactivated_robots()

    for robot in battle.deactivated_robots:
        assert robot.position is not None


def test_attack_subtract_hp_of_attacked_deactivated_robot():
    battle = Battle()
    red_robot = get_robot(battle, (3, 3), red=True)
    deactivated_robot = get_robot(battle, (2, 3))

    battle.attack(red_robot)

    assert deactivated_robot.hp == 0


def test_after_death_deactivated_robot_is_removed():
    battle = Battle()
    battle.arena.init()
    battle._set_deactivated_robots()
    robot = battle.deactivated_robots[2]

    battle.destroy(robot)

    assert len(battle.deactivated_robots) == 7
    assert robot not in battle.deactivated_robots


def test_drop_item_when_robot_destroyed():
    battle = Battle()
    robot = get_robot(battle, (2, 3))

    battle.destroy(robot)

    assert battle.arena.board[2][3] == '*'
    assert isinstance(battle.items[0], Item)


def test_drop_item_drops_random_weapon_or_body():
    random.seed(2021)
    battle = Battle()

    battle.drop_item((2, 3))

    assert battle.items == [body.LightBody()]


def test_pick_item_weapon_add_it_to_its_weapons():
    random.seed(1)
    battle = Battle()
    robot = get_robot(battle, (2, 4), red=True)

    battle.drop_item((2, 4))
    battle.pick_item(robot)

    assert len(robot.weapons) == 2
    assert battle.items == []


def test_pick_item_if_robot_stands_on_items_field():
    random.seed(2021)
    battle = Battle()
    robot = get_robot(battle, (2, 3), red=True)
    battle.drop_item((2, 4))

    battle.move(robot, Move.RIGHT)

    assert battle.red_robot.bodies == [body.SimpleBody(), body.LightBody()]
    assert battle.items == []


def test_select_weapon_successfully():
    battle = Battle()
    robot = get_robot(battle, (2, 3), red=True)
    robot.weapons.append(weapon.Explosion())

    battle.select_weapon(robot, 1)

    assert battle.red_robot.selected_weapon == weapon.Explosion()


def test_select_body_successfully():
    battle = Battle()
    robot = get_robot(battle, (2, 3), red=True)
    robot.bodies.append(body.BattleBody())

    battle.select_body(robot, 1)

    assert battle.red_robot.selected_body == body.BattleBody()


def test_select_extra_weapon_successfully():
    battle = Battle()
    robot = get_robot(battle, (2, 3), red=True)
    robot.pick(weapon.Explosion())
    robot.extra_slot = True

    battle.select_extra_weapon(robot, 1)

    assert battle.red_robot.extra_weapon == weapon.Explosion()


def test_activated_robot_is_destroyed_if_its_hp_is_zero():
    battle = Battle()
    red_robot = get_robot(battle, (3, 3), red=True)
    blue_robot = get_robot(battle, (2, 3), blue=True)

    battle.attack(red_robot)
    battle.attack(red_robot)

    assert blue_robot.hp == 0

