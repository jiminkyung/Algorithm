# 분할 정복

# 메모리: 31120KB / 시간: 92ms
# 단순 행렬 곱셈 문제인듯.

from sys import stdin


input = stdin.readline
N, M = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]

M, K = map(int, input().split())
B = [list(map(int, input().split())) for _ in range(M)]

ret = [[0]*K for _ in range(N)]

def make_matrix(row, col):
    tmp = 0

    for i in range(M):
        tmp += A[row][i] * B[i][col]
    
    return tmp

for i in range(N):
    for j in range(K):
        ret[i][j] = make_matrix(i, j)

for r in ret:
    print(" ".join(str(x) for x in r))