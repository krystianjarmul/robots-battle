from typing import List


def turn_matrix(X: List[List[int]], times: int = 1) -> List[List[int]]:
    if not times:
        return X

    if times:
        X_T = [[X[j][i] for j in range(len(X))] for i in range(len(X))]
        X_turned = [row[::-1] for row in X_T]
        times -= 1
        return turn_matrix(X_turned, times)
