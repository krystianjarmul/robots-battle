import random
import enum
from typing import Tuple


class Move(enum.Enum):
    UP = 0
    RIGHT = 1
    DOWN = 2
    LEFT = 3


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

    def move(self, pos: Tuple[int, int], move: Move):
        if move.name == 'UP':
            dst = pos[0] - 1
            if dst < 0:
                dst = 0
            self.board[pos[0]][pos[1]] = 0
            self.board[dst][pos[1]] = 'x'

        elif move.name == 'DOWN':
            dst = pos[0] + 1
            if dst > 5:
                dst = 5
            self.board[pos[0]][pos[1]] = 0
            self.board[dst][pos[1]] = 'x'

        elif move.name == 'LEFT':
            dst = pos[1] - 1
            if dst < 0:
                dst = 0
            self.board[pos[0]][pos[1]] = 0
            self.board[pos[0]][dst] = 'x'

        elif move.name == 'RIGHT':
            dst = pos[1] + 1
            if dst > 5:
                dst = 5
            self.board[pos[0]][pos[1]] = 0
            self.board[pos[0]][dst] = 'x'
