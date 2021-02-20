class Body:

    def __init__(self):
        self.name: str
        self.hp: str


class SimpleBody(Body):

    def __init__(self):
        super().__init__()
        self.name = 'Simple Body'
        self.hp = 2


class HardBody(Body):

    def __init__(self):
        super().__init__()
        self.name = 'Hard Body'
        self.hp = 5


class LightBody(Body):

    def __init__(self):
        super().__init__()
        self.name = 'Light Body'
        self.hp = 3
        self.movement = 1


class BattleBody(Body):

    def __init__(self):
        super().__init__()
        self.name = 'Battle Body'
        self.hp = 2
        self.adds_slot = True
