from typing import List, Tuple


def get_turned_matrix(X: List[List[int]], times: int = 1) -> List[List[int]]:
    if not times:
        return X

    if times:
        X_T = [[X[j][i] for j in range(len(X))] for i in range(len(X))]
        X_turned = [row[::-1] for row in X_T]
        times -= 1
        return get_turned_matrix(X_turned, times)


def get_shift(facing: List[int], number: int) -> Tuple[int, int]:
    facing_idx = facing.index(1)
    if facing_idx == 0:
        return -number, 0
    elif facing_idx == 1:
        return 0, number
    elif facing_idx == 2:
        return number, 0
    elif facing_idx == 3:
        return 0, -number
