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