from src.utils import get_turned_matrix, get_shift


def test_turn_matrix_once():
    X = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]

    X_turned = get_turned_matrix(X)

    assert X_turned == [
        [7, 4, 1],
        [8, 5, 2],
        [9, 6, 3]
    ]


def test_turn_matrix_couple_times():
    X = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]

    X_turned = get_turned_matrix(X, 2)

    assert X_turned == [
        [9, 8, 7],
        [6, 5, 4],
        [3, 2, 1]
    ]


def test_get_position_with_proper_signs():
    facing_north = [1, 0, 0, 0]
    facing_east = [0, 1, 0, 0]
    facing_south = [0, 0, 1, 0]
    facing_west = [0, 0, 0, 1]

    x1, y1 = get_shift(facing_north, 1)
    x2, y2 = get_shift(facing_east, 1)
    x3, y3 = get_shift(facing_south, 1)
    x4, y4 = get_shift(facing_west, 1)

    assert x1 == -1
    assert y2 == 1
    assert x3 == 1
    assert y4 == -1
    assert [y1, x2, y3, x4] == [0, 0, 0, 0]

