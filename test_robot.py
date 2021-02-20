from robot import Robot, Team


def test_robot_belongs_to_blue_or_read_team():
    robot1 = Robot(Team.BLUE)
    robot2 = Robot(Team.RED)
    assert robot1.team == Team.BLUE
    assert robot2.team == Team.RED

