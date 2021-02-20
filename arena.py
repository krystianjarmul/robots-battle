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

    def set_deactivated_robots(self):
        battleground = self.board[1:-1]
        for _ in range(8):
            while True:
                idx = random.randint(0, 5)
                row = random.randint(0, 3)
                if battleground[row][idx] == 'x':
                    continue
                battleground[row][idx] = 'x'
                break

    def init(self):
        self.set_blue_team()
        self.set_red_team()
        self.set_deactivated_robots()





