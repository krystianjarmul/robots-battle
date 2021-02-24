from src import weapon


def test_basic_shot_attributes():
    basic_shoot = weapon.BasicShot()
    assert basic_shoot.directions == [[0, 1, 0], [0, 0, 0], [0, 0, 0]]
    assert basic_shoot.range == [[0, 2, 0], [0, 0, 0], [0, 0, 0]]


def test_laser_attributes():
    laser = weapon.Laser()
    assert laser.directions == [[0, 1, 0], [0, 0, 0], [0, 0, 0]]
    assert laser.range == [[0, 5, 0], [0, 0, 0], [0, 0, 0]]


def test_sword_attributes():
    sword = weapon.Sword()
    assert sword.directions == [[1, 1, 1], [0, 0, 0], [0, 0, 0]]
    assert sword.range == [[1, 1, 1], [0, 0, 0], [0, 0, 0]]


def test_explosion_attributes():
    explosion = weapon.Explosion()
    assert explosion.directions == [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
    assert explosion.range == [[1, 1, 1], [1, 0, 1], [1, 1, 1]]


def test_dual_laser_attributes():
    dual_laser = weapon.DualLaser()
    assert dual_laser.directions == [[0, 0, 0], [1, 0, 1], [0, 0, 0]]
    assert dual_laser.range == [[0, 0, 0], [5, 0, 5], [0, 0, 0]]
