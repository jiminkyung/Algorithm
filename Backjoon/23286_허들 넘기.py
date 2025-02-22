# 문제집 - 0x1C강 - 플로이드 알고리즘


# 문제: https://www.acmicpc.net/problem/23286

# 일반적인 플로이드-워셜과는 다른 문제.
# ⭐ Python3로 통과하려면 다익스트라를 활용해야함.

# PyPy3로 통과한 풀이 (플로이드-워셜)
# 메모리: 112040KB / 시간: 508ms
from sys import stdin


input = stdin.readline
INF = int(1e9)

N, M, T = map(int, input().split())
graph = [[INF] * (N+1) for _ in range(N+1)]

for _ in range(M):
    u, v, h = map(int, input().split())
    graph[u][v] = h

# 만약 허들이 1 + 3 + 1 이렇게 있고, 1 + 1 + 1 + 1 + 1 + 1 이렇게 있다면?
# 허들의 총 높이값은 전자가 작지만, 최대 허들높이는 후자가 더 작아지게 됨.

for k in range(1, N+1):
    graph[k][k] = 0
    for i in range(1, N+1):
        for j in range(1, N+1):
            # new = max(i-k에서 가장 높은 허들, k-j에서 가장 높은 허들)
            new = max(graph[i][k], graph[k][j])

            # i-k, k-j 모두 경로가 존재하는 경우에만 업데이트
            # graph[i][j] = min(new 허들 높이, 기존 허들 높이)
            if graph[i][k] != INF and graph[k][j] != INF:
                graph[i][j] = min(new, graph[i][j])

for _ in range(T):
    s, e = map(int, input().split())
    print(graph[s][e] if graph[s][e] != INF else -1)


# ⭐ Python3로 통과한 풀이 (다익스트라)
# 참고👉 https://www.acmicpc.net/source/67136422
# 메모리: 37452KB / 시간: 600ms
from sys import stdin
from collections import defaultdict
from heapq import heappop, heappush


input = stdin.readline
INF = int(1e9)

N, M, T = map(int, input().split())
# 2차원 딕셔너리 생성
# graph[a][b] = {a: {b: 허들 높이}}
graph = defaultdict(dict)

for _ in range(M):
    u, v, h = map(int, input().split())
    graph[u][v] = h


def dijkstra(start):
    queue = []
    heappush(queue, (0, start))

    while queue:
        curr_h, curr = heappop(queue)

        if heights[start][curr] < curr_h:
            continue

        for nxt, h in graph[curr].items():
            new_h = max(h, curr_h)
            if new_h < heights[start][nxt]:
                heights[start][nxt] = new_h
                heappush(queue, (new_h, nxt))


heights = [[INF] * (N+1) for _ in range(N+1)]

# 다익스트라로 모든 노드를 시작점으로 두고 최단경로 구하기
for i in range(1, N+1):
    heights[i][i] = 0
    dijkstra(i)

for _ in range(T):
    s, e = map(int, input().split())
    ret = heights[s][e]
    print(ret if ret != INF else -1)