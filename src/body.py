from src.base import Item


class Body(Item):

    def __init__(self):
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
        self.name = 'SIMPLE BODY'
        self.hp = 2


class HardBody(Body):

    def __init__(self):
        super().__init__()
        self.name = 'HARD BODY'
        self.hp = 5


class LightBody(Body):

    def __init__(self):
        super().__init__()
        self.name = 'LIGHT BODY'
        self.hp = 3
        self.movement = 1


class BattleBody(Body):

    def __init__(self):
        super().__init__()
        self.name = 'BATTLE BODY'
        self.hp = 2
        self.extra_slot = True
