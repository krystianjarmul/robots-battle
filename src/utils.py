from typing import List

from src.base import Matrix, Position


def get_turned_matrix(X: Matrix, times: int = 1) -> Matrix:
    if not times:
        return X

    if times:
        X_T = [[X[j][i] for j in range(len(X))] for i in range(len(X))]
        X_turned = [row[::-1] for row in X_T]
        times -= 1
        return get_turned_matrix(X_turned, times)


def get_shift(facing: List[int], number: int) -> Position:
    facing_idx = facing.index(1)
    if facing_idx == 0:
        return -number, 0

    elif facing_idx == 1:
        return 0, number

    elif facing_idx == 2:
        return number, 0

    elif facing_idx == 3:
        return 0, -number


def is_field_correct(field: Position) -> bool:
    field_indices = list(range(0, 6))
    if field[0] not in field_indices or field[1] not in field_indices:
        return False
    return True


def validate_fields(fields: List[Position]) -> List[Position]:
    return [field for field in fields if is_field_correct(field)]
