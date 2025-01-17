# 문제집 - 0x18강 - 그래프


# 문제: https://www.acmicpc.net/problem/11403
# 메모리: 33432KB / 시간: 340ms
from sys import stdin


input = stdin.readline

N = int(input())
INF = float("inf")
graph = [[INF] * N for _ in range(N)]

for i in range(N):
    line = list(map(int, input().split()))
    # graph[i][i] = 0  # i -> i 초기화 X
    for j in range(N):
        if line[j]:
            graph[i][j] = 1

# 플로이드-워셜 수행
for k in range(N):
    for i in range(N):
        for j in range(N):
            graph[i][j] = min(graph[i][k] + graph[k][j], graph[i][j])

for row in range(N):
    for col in range(N):
        if graph[row][col] == INF:
            graph[row][col] = 0
        else:
            graph[row][col] = 1
    print(*graph[row])