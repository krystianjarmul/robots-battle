from src import weapon
from src.robot import ActivatedRobot, Team, Robot, Direction, DeactivatedRobot
from src.body import SimpleBody
from src.weapon import BasicShot


def test_robot_belongs_to_blue_or_read_team():
    robot1 = ActivatedRobot(Team.BLUE)
    robot2 = ActivatedRobot(Team.RED)
    assert robot1.team == Team.BLUE
    assert robot2.team == Team.RED


def test_robot_at_start_has_default_attributes():
    robot = ActivatedRobot(Team.BLUE)
    assert robot.bodies == [SimpleBody(), ]
    assert robot.weapons == [BasicShot(), ]
    assert robot.hp == 2
    assert robot.movement == 1
    assert robot.weapon_slots == 1


def test_robot_turn_right_changes_its_facing():
    robot = ActivatedRobot(Team.RED)

    robot.turn(Direction.EAST)

    assert robot.facing == [0, 1, 0, 0]


def test_robot_turn_down_changes_its_facing():
    robot = ActivatedRobot(Team.RED)

    robot.turn(Direction.SOUTH)

    assert robot.facing == [0, 0, 1, 0]


def test_robot_turn_left_changes_its_facing():
    robot = ActivatedRobot(Team.RED)

    robot.turn(Direction.WEST)

    assert robot.facing == [0, 0, 0, 1]


def test_robot_turn_left_changes_its_facing():
    robot = ActivatedRobot(Team.RED)
    robot.facing = [0, 0, 0, 1]

    robot.turn(Direction.NORTH)

    assert robot.facing == [1, 0, 0, 0]


def test_robot_attack_returns_weapon():
    robot = ActivatedRobot(Team.RED)
    weapon = robot.attack()

    assert weapon.directions == [[0, 1, 0], [0, 0, 0], [0, 0, 0]]
    assert weapon.range == [[0, 2, 0], [0, 0, 0], [0, 0, 0]]


def test_deactivated_robot_has_id_attribute():
    robot = DeactivatedRobot(1)
    assert robot.id == 1


def test_is_alive_checks_current_robot_hp():
    robot1 = DeactivatedRobot(1)
    robot2 = DeactivatedRobot(2)
    robot2.hp -= 1

    assert robot1.is_alive()
    assert robot2.is_alive() is False


