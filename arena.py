import random


class Arena:

    def __init__(self):
        self.board: [List[List[int]]] = [
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
        ]
        self.robot = 'x'
        self.item = '*'

    def set_blue_team(self):
        idx = random.randint(0, 5)
        self.board[0][idx] = 'x'

    def set_red_team(self):
        idx = random.randint(0, 5)
        self.board[-1][idx] = 'x'
