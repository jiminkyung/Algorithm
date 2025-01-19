# 문제집 - 0x18강 - 그래프


# 문제: https://www.acmicpc.net/problem/1389
# 메모리: 33432KB / 시간: 368ms
from sys import stdin


input = stdin.readline

N, M = map(int, input().split())
INF = float("inf")

graph = [[INF] * N for _ in range(N)]

for i in range(N):
    graph[i][i] = 0

for _ in range(M):
    u, v = map(int, input().split())
    graph[u-1][v-1] = 1
    graph[v-1][u-1] = 1

# 플로이드-워셜 수행
for k in range(N):
    for i in range(N):
        for j in range(N):
            graph[i][j] = min(graph[i][k] + graph[k][j], graph[i][j])

min_bacon = INF  # 현재까지 나온 케빈 베이컨의 수 중 최솟값
number = 0  # 최솟값인 사람의 번호

for i in range(N):
    bacon = 0
    for j in range(N):
        bacon += graph[i][j]
    
    if bacon < min_bacon:
        min_bacon = bacon
        number = i

print(number+1)