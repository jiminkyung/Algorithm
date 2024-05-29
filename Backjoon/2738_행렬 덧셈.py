# 프로그래머스와 달라서 당황스럽다.

N, M = map(int, input().split())

A, B = [], []

for _ in range(N):
    row = list(map(int, input().split()))
    A.append(row)

for _ in range(N):
    row = list(map(int, input().split()))
    B.append(row)

for i in range(N):
    tmp = []
    for k in range(M):
        tmp.append(A[i][k] + B[i][k])
    print(*tmp)