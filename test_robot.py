from robot import Robot, Team
import body
import weapon


def test_robot_belongs_to_blue_or_read_team():
    robot1 = Robot(Team.BLUE)
    robot2 = Robot(Team.RED)
    assert robot1.team == Team.BLUE
    assert robot2.team == Team.RED


def test_robot_at_start_has_default_attributes():
    robot = Robot(Team.BLUE)
    assert robot.body == body.SimpleBody()
    assert robot.weapon == weapon.BasicShot()
    assert robot.hp == 2
    assert robot.movement == 1


