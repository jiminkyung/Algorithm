# 문제집 - 0x1C강 - 플로이드 알고리즘


# 문제: https://www.acmicpc.net/problem/11562
# 메모리: 34456KB / 시간: 4928ms
from sys import stdin


input = stdin.readline
INF = int(1e9)

N, M = map(int, input().split())
graph = [[INF] * (N+1) for _ in range(N+1)]

# 건설되어 있는 도로(양방향, 일반도로 u -> v)라면 0으로 설정.
# 일반 도로에서 역방향, v -> u의 값은 1로 설정한다.
# => 건설되지 않은 역방향 도로 v -> u가 최단거리에 포함되는 갯수 = 양방향 도로로 변경해야하는 도로의 갯수
for _ in range(M):
    u, v, b = map(int, input().split())
    
    graph[u][v] = 0
    graph[v][u] = 0

    if b == 0:
        graph[v][u] = 1


for k in range(1, N+1):
    graph[k][k] = 0
    for i in range(1, N+1):
        for j in range(1, N+1):
            graph[i][j] = min(graph[i][k] + graph[k][j], graph[i][j])


K = int(input())
for _ in range(K):
    s, e = map(int, input().split())
    print(graph[s][e])