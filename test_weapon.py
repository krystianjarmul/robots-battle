import weapon


def test_basic_shot_attributes():
    basic_shoot = weapon.BasicShot()
    assert basic_shoot.directions == [0, 1, 0, 0, 0, 0, 0, 0, 0]
    assert basic_shoot.range == [0, 2, 0, 0, 0, 0, 0, 0, 0]

