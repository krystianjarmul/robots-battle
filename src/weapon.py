from src.base import Item


class Weapon(Item):

    def __init__(self):
        self.directions: List[int]
        self.range: List[int]

    def __eq__(self, other):
        if not isinstance(other, Weapon):
            return False
        return other.range == self.range

    def __hash__(self):
        return hash(self.range)


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
