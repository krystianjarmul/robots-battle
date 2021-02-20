class Body:

    def __init__(self):
        self.name: str
        self.hp: str

    def __eq__(self, other):
        if not isinstance(other, Body):
            return False
        return other.name == self.name

    def __hash__(self):
        return hash(self.name)


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
