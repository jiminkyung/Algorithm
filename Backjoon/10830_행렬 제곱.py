# 분할 정복

"""
A^B일때,
B % 2 == 0이면,
    half = B//2
    A^half * A^half
아니면,
    A * A^half * A^half
    즉, A * A^(B-1)
"""

# 메모리: 31252KB / 시간: 44ms

from sys import stdin


input = stdin.readline
N, B = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]
p = 1000
# ❗ 주어진 A의 원소 입력값들도 1000으로 나누어줘야한다. A = [[1000, 1000], [1000, 1000]]으로 주어질수도 있음.
A = [[col % p for col in row] for row in A]


def make_matrix(arr1: list, arr2: list) -> list:
    tmp = [[0]*N for _ in range(N)]

    for i in range(N):
        for j in range(N):
            for k in range(N):
                tmp[i][j] += arr1[i][k] * arr2[k][j]
            tmp[i][j] %= p
    
    return tmp


def make_square(arr: list, n: int) -> list:
    if n == 1:
        return arr
    
    if n % 2 == 0:
        half = make_square(arr, n//2)
        return make_matrix(half, half)
    else:
        return make_matrix(arr, make_square(arr, n-1))


ret = make_square(A, B)

for line in ret:
    print(" ".join(str(l) for l in line))