from src import weapon
from src import body
from src.robot import ActivatedRobot, Team, Robot, Direction, DeactivatedRobot


def test_robot_belongs_to_blue_or_read_team():
    robot1 = ActivatedRobot(Team.BLUE)
    robot2 = ActivatedRobot(Team.RED)
    assert robot1.team == Team.BLUE
    assert robot2.team == Team.RED


def test_robot_at_start_has_default_attributes():
    robot = ActivatedRobot(Team.BLUE)
    assert robot.bodies == [body.SimpleBody(), ]
    assert robot.weapons == [weapon.BasicShot(), ]
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


def test_is_alive_checks_current_robot_hp():
    robot1 = DeactivatedRobot()
    robot2 = DeactivatedRobot()
    robot2.hp -= 1

    assert robot1.is_alive()
    assert robot2.is_alive() is False


def test_select_weapon_successfully():
    robot = ActivatedRobot(Team.RED)
    robot.weapons.append(weapon.Laser())

    robot.select_weapon(1)

    assert robot.selected_weapon == weapon.Laser()


def test_cannot_select_weapon_if_weapon_index_not_exist():
    robot = ActivatedRobot(Team.RED)
    robot.weapons.append(weapon.Laser())

    robot.select_weapon(2)

    assert robot.selected_weapon == weapon.BasicShot()


def test_pick_add_item_to_weapons_or_bodies():
    robot = ActivatedRobot(Team.RED)

    robot.pick(weapon.Laser())

    assert robot.weapons == [weapon.BasicShot(), weapon.Laser()]


def test_weapons_are_unique():
    robot = ActivatedRobot(Team.RED)

    robot.pick(weapon.Laser())
    robot.pick(weapon.Laser())

    assert robot.weapons == [weapon.BasicShot(), weapon.Laser()]


def test_bodies_are_unique():
    robot = ActivatedRobot(Team.RED)

    robot.pick(body.HardBody())
    robot.pick(body.HardBody())

    assert robot.bodies == [body.SimpleBody(), body.HardBody()]


def test_robot_can_select_a_body():
    robot = ActivatedRobot(Team.BLUE)
    robot.pick(body.HardBody())

    robot.select_body(1)

    assert robot.selected_body == body.HardBody()


def test_wear_hard_body_increases_robot_hp():
    robot = ActivatedRobot(Team.BLUE)
    robot.pick(body.HardBody())

    robot.select_body(1)

    assert robot.hp == body.HardBody().hp


def test_wear_light_body_increases_robot_hp_and_movement():
    robot = ActivatedRobot(Team.BLUE)
    robot.pick(body.LightBody())

    robot.select_body(1)

    assert robot.hp == body.LightBody().hp
    assert robot.movement == body.LightBody().movement


def test_wear_battle_body_increases_robot_add_extra_weapon_slot():
    robot = ActivatedRobot(Team.BLUE)
    robot.pick(body.BattleBody())

    robot.select_body(1)

    assert robot.extra_slot == body.BattleBody().extra_slot


def test_cannot_select_extra_weapon_if_not_extra_slot():
    robot = ActivatedRobot(Team.BLUE)
    robot.pick(weapon.Laser())
    robot.pick(weapon.Sword())

    robot.select_extra_weapon(2)

    assert robot.extra_weapon is None


def test_select_extra_weapon_successfully():
    robot = ActivatedRobot(Team.BLUE)
    robot.pick(weapon.Laser())
    robot.pick(weapon.Sword())
    robot.extra_slot = True

    robot.select_extra_weapon(2)

    assert robot.extra_weapon == weapon.Sword()


def test_cannot_select_extra_weapon_if_slot_is_busy():
    robot = ActivatedRobot(Team.BLUE)
    robot.pick(weapon.Laser())
    robot.pick(weapon.Sword())
    robot.extra_slot = True

    robot.select_extra_weapon(0)

    assert robot.extra_weapon is None


def test_select_extra_weapon_for_the_same_slot_does_nothing():
    robot = ActivatedRobot(Team.BLUE)
    robot.pick(weapon.Laser())
    robot.pick(weapon.Sword())
    robot.extra_slot = True

    robot.select_extra_weapon(2)
    robot.select_extra_weapon(2)

    assert robot.extra_weapon == weapon.Sword()


def test_attack_returns_extra_weapon_if_extra_parameter():
    robot = ActivatedRobot(Team.BLUE)
    robot.pick(weapon.Laser())
    robot.extra_slot = True
    robot.select_extra_weapon(1)

    extra_weapon = robot.attack(extra=True)

    assert extra_weapon == weapon.Laser()
