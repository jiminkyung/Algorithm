# 문제집 - 0x1C강 - 플로이드 알고리즘


# 문제: https://www.acmicpc.net/problem/14938
# 메모리: 33432KB / 시간: 328ms
from sys import stdin


input = stdin.readline
INF = float("inf")

n, m, r = map(int, input().split())
graph = [[INF] * n for _ in range(n)]

item = list(map(int, input().split()))

for i in range(n):
    graph[i][i] = 0

for _ in range(r):
    a, b, l = map(int, input().split())
    graph[a-1][b-1] = l
    graph[b-1][a-1] = l

# 플로이드-워셜 수행
# 한 노드에서 다른 모든 노드까지의 최단거리 구하기
for k in range(n):
    for i in range(n):
        for j in range(n):
            graph[i][j] = min(graph[i][k] + graph[k][j], graph[i][j])

max_get = 0

for target in range(n):
    get = 0

    for node in range(n):
        # 최단거리가 m 이하인 구역의 아이템만 주울 수 있음
        if graph[target][node] <= m:
            get += item[node]
    
    max_get = max(get, max_get)

print(max_get)