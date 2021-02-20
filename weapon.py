class Weapon:

    def __init__(self):
        directions: List[int]
        range: List[int]


class BasicShot(Weapon):

    def __init__(self):
        super().__init__()
        self.directions = [0, 1, 0, 0, 0, 0, 0, 0, 0]
        self.range = [0, 2, 0, 0, 0, 0, 0, 0, 0]


class Laser(Weapon):

    def __init__(self):
        super().__init__()
        self.directions = [0, 1, 0, 0, 0, 0, 0, 0, 0]
        self.range = [0, 5, 0, 0, 0, 0, 0, 0, 0]


class Sword(Weapon):

    def __init__(self):
        super().__init__()
        self.directions = [1, 1, 1, 0, 0, 0, 0, 0, 0]
        self.range = [1, 1, 1, 0, 0, 0, 0, 0, 0]


class Explosion(Weapon):

    def __init__(self):
        super().__init__()
        self.directions = [1, 1, 1, 1, 0, 1, 1, 1, 1]
        self.range = [1, 1, 1, 1, 0, 1, 1, 1, 1]


class DualLaser(Weapon):

    def __init__(self):
        super().__init__()
        self.directions = [0, 0, 0, 1, 0, 1, 0, 0, 0]
        self.range = [0, 0, 0, 5, 0, 5, 0, 0, 0]