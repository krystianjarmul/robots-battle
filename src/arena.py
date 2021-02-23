import random
from typing import Tuple

from src.base import Move


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
        self.robot: str = 'x'
        self.item: str = '*'

    def set_red_team(self):
        idx = random.randint(0, 5)
        self.board[0][idx] = 'x'

    def set_blue_team(self):
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
        self.set_red_team()
        # self.set_blue_team()
        # self.set_deactivated_robots()

    def move(self, pos: Tuple[int, int], move: Move):
        if move.name == 'UP':
            dest = pos[0] - 1
            if dest < 0:
                dest = 0
            elif self.board[dest][pos[1]] == 'x':
                dest = pos[0]
            self.board[pos[0]][pos[1]] = 0
            self.board[dest][pos[1]] = 'x'
            x, y = dest, pos[1]

        elif move.name == 'DOWN':
            dest = pos[0] + 1
            if dest > 5:
                dest = 5
            elif self.board[dest][pos[1]] == 'x':
                dest = pos[0]
            self.board[pos[0]][pos[1]] = 0
            self.board[dest][pos[1]] = 'x'
            x, y = dest, pos[1]

        elif move.name == 'LEFT':
            dest = pos[1] - 1
            if dest < 0:
                dest = 0
            elif self.board[pos[0]][dest] == 'x':
                dest = pos[1]
            self.board[pos[0]][pos[1]] = 0
            self.board[pos[0]][dest] = 'x'
            x, y = pos[0], dest

        elif move.name == 'RIGHT':
            dest = pos[1] + 1
            if dest > 5:
                dest = 5
            elif self.board[pos[0]][dest] == 'x':
                dest = pos[1]
            self.board[pos[0]][pos[1]] = 0
            self.board[pos[0]][dest] = 'x'
            x, y = pos[0], dest

        return (x, y)
