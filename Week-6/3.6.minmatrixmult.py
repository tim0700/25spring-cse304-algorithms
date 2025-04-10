from typing import Tuple

def minimum(i: int, j: int, M: list[list[float]], d: list[int]) -> Tuple[float, int]:
    minvalue: float = INF
    mink: int = 0
    for k in range(i, j):
        # Complete the code here

        q = M[i][k] + M[k + 1][j] + d[i - 1] * d[k] * d[j]
        if q < minvalue:
            minvalue = q
            mink = k

    return minvalue, mink

def minmult(n: int, d: list[int]) -> Tuple[float, list[list[float]], list[list[int]]]:
    M: list[list[float]] = [[INF] * (n + 1) for _ in range(n + 1)]
    P: list[list[int]] = [[0] * (n + 1) for _ in range(n + 1)]
    for i in range(n + 1):
        M[i][i] = 0
    for diagonal in range(1, n):
        # Complete the code here
        # Tip. Implement minimum() and use it

        for i in range (1, n-diagonal + 1):
            j = i + diagonal
            M[i][j], P[i][j] = minimum(i, j, M, d)

        pass
    return M[1][n], M, P

def order(i: int, j: int, P: list[list[int]]) -> str:
    if i == j:
        return "A" + str(i)
    else:
        # Complete the code here 
        k = P[i][j]
        return "(" + order(i, k, P) + order(k + 1, j, P) + ")"

        pass

INF: float = float("inf")