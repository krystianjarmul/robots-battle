import random

from src.base import Move, Matrix, Position


class Arena:

    def __init__(self):
        self.board: Matrix = [
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
        ]
        self.robot: str = 'x'
        self.item: str = '*'

    def init(self):
        self._set_red_team()
        self._set_blue_team()
        self._set_deactivated_robots()

    def move(self, source: Position, move: Move):
        source_y = source[0]
        source_x = source[1]
        is_item = False
        can_move = True
        if move.name == 'UP':
            destination_y = source_y - 1
            if destination_y < 0:
                destination_y = 0
                can_move = False

            elif self.board[destination_y][source_x] == 'x':
                can_move = False
                destination_y = source_y

            elif self.board[destination_y][source_x] == '*':
                is_item = True

            destination = self._get_destination(source, destination_y, move)

        elif move.name == 'DOWN':
            destination_y = source_y + 1
            if destination_y > 5:
                can_move = False
                destination_y = 5

            elif self.board[destination_y][source_x] == 'x':
                destination_y = source_y
                can_move = False

            elif self.board[destination_y][source_x] == '*':
                is_item = True

            destination = self._get_destination(source, destination_y, move)

        elif move.name == 'LEFT':
            destination_x = source_x - 1
            if destination_x < 0:
                destination_x = 0
                can_move = False

            elif self.board[source_y][destination_x] == 'x':
                destination_x = source_x
                can_move = False

            elif self.board[source_y][destination_x] == '*':
                is_item = True

            destination = self._get_destination(source, destination_x, move)

        elif move.name == 'RIGHT':
            destination_x = source_x + 1
            if destination_x > 5:
                destination_x = 5
                can_move = False

            elif self.board[source_y][destination_x] == 'x':
                destination_x = source_x
                can_move = False

            elif self.board[source_y][destination_x] == '*':
                is_item = True

            destination = self._get_destination(source, destination_x, move)

        return can_move, is_item

    def drop_item(self, position: Position):
        self.board[position[0]][position[1]] = '*'

    def _set_red_team(self):
        idx = random.randint(0, 5)
        self.board[0][idx] = 'x'

    def _set_blue_team(self):
        idx = random.randint(0, 5)
        self.board[-1][idx] = 'x'

    def _set_deactivated_robots(self):
        battleground = self.board[1:-1]
        for _ in range(8):
            while True:
                idx = random.randint(0, 5)
                row = random.randint(0, 3)
                if battleground[row][idx] == 'x':
                    continue

                battleground[row][idx] = 'x'
                break

    def _get_destination(self, src: Position, dst: int, move: Move) -> Position:
        src_y, src_x = src
        self.board[src_y][src_x] = 0
        if move.name in ['UP', 'DOWN']:
            self.board[dst][src_x] = 'x'
            destination = (dst, src_x)

        elif move.name in ['LEFT', 'RIGHT']:
            self.board[src_y][dst] = 'x'
            destination = (src_y, dst)

        return destination
