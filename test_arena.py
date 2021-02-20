import random

from arena import Arena, Move


def set_robot_in_center(board):
    board[2][3] = 'x'


def test_arena_is_square_6x6():
    arena = Arena()
    assert len(arena.board) == 6
    for row in arena.board:
        assert len(row) == 6


def test_arena_default_has_all_fields_fill_with_zeros():
    arena = Arena()
    assert any([field == 0 for row in arena.board for field in row])


def test_arena_object_symbol():
    arena = Arena()
    assert arena.robot == 'x'
    assert arena.item == '*'


def test_sets_a_blue_team_robot_its_starting_area():
    arena = Arena()

    arena.set_blue_team()

    assert 'x' in arena.board[0]


def test_sets_a_red_team_robot_in_its_starting_area():
    arena = Arena()

    arena.set_red_team()

    assert 'x' in arena.board[-1]


def test_sets_8_deactivated_robots_in_battleground():
    arena = Arena()

    arena.set_deactivated_robots()

    assert sum([row.count('x') for row in arena.board]) == 8


def test_init_sets_all_robots_on_board():
    arena = Arena()

    arena.init()

    assert sum([row.count('x') for row in arena.board]) == 10


def test_move_up_successfully():
    arena = Arena()

    set_robot_in_center(arena.board)

    arena.move((2, 3), Move.UP)

    assert arena.board[1][3] == 'x'
    assert arena.board[2][3] == 0


def test_move_down_successfully():
    arena = Arena()

    set_robot_in_center(arena.board)

    arena.move((2, 3), Move.DOWN)

    assert arena.board[3][3] == 'x'
    assert arena.board[2][3] == 0


def test_move_left_successfully():
    arena = Arena()

    set_robot_in_center(arena.board)

    arena.move((2, 3), Move.LEFT)

    assert arena.board[2][2] == 'x'
    assert arena.board[2][3] == 0

