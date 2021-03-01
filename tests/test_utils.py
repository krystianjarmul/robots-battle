from src.base import Direction
from src.utils import get_turned_matrix, get_shift, is_field_correct, \
    validate_fields


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

    x1, y1 = get_shift(facing_north, 1, Direction.NORTH)
    x2, y2 = get_shift(facing_east, 1, Direction.NORTH)
    x3, y3 = get_shift(facing_south, 1, Direction.NORTH)
    x4, y4 = get_shift(facing_west, 1, Direction.NORTH)

    assert x1 == -1
    assert y2 == 1
    assert x3 == 1
    assert y4 == -1
    assert [y1, x2, y3, x4] == [0, 0, 0, 0]


def test_field_is_validated():
    field1 = (3, 3)
    field2 = (3, 7)
    field3 = (6, 6)
    field4 = (6, 2)
    field5 = (4, 7)
    field6 = (1, 8)

    assert is_field_correct(field1)
    assert not is_field_correct(field2)
    assert not is_field_correct(field3)
    assert not is_field_correct(field4)
    assert not is_field_correct(field5)
    assert not is_field_correct(field6)


def test_validate_attack_fields():
    fields = [(3, 5), (3, 6), (5, 8), (1, 8)]

    fields = validate_fields(fields)

    assert fields == [(3, 5)]
