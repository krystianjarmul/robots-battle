class Weapon:

    def __init__(self):
        directions: List[int]
        range: List[int]


class BasicShot(Weapon):

    def __init__(self):
        super().__init__()
        self.directions = [0, 1, 0, 0, 0, 0, 0, 0, 0]
        self.range = [0, 2, 0, 0, 0, 0, 0, 0, 0]
