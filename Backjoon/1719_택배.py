# 문제집 - 0x1C강 - 플로이드 알고리즘


# 문제: https://www.acmicpc.net/problem/1719

# 처음엔 container[i][j] = k 로 설정했다가 실패. 아래의 질문글을 보고 이해했다.
"""
출처: https://www.acmicpc.net/board/view/104174

예를 들어 1에서 3으로 이동하는 최단거리가 1 - 2 - 3 이라고 하면 k = 2 일 때 갱신되며 tmp[1][3] = 2 가 됩니다. (graph[1][3] = graph[1][2] + graph[2][3], 제일 먼저 2를 방문)
여기서 1에서 4로 가는 최단거리가 1 - 2 - 3 - 4이라고 하면, k = 3일 때 graph[1][4]가 갱신됩니다. (graph[1][4] = graph[1][3] + graph[3][4], 제일 먼저 2를 방문)
이 때, 1 - 2 - 3 - 4 는 k = 2 일 때 갱신되지 않습니다. (k = 2 일때 갱신되려면 graph[1][4] = graph[1][2] + graph[2][4] 여야 하는데 graph[2][4](2 - 3 - 4)는 k = 3 일때 갱신)
즉, tmp[1][4] = 2인데 tmp[i][j] = k면 tmp[1][4] = 3이 되어 틀리게 됩니다.
"""
# 메모리: 33432KB / 시간: 1984ms
from sys import stdin


input = stdin.readline
INF = int(1e9)

N, M = map(int, input().split())
graph = [[INF] * (N+1) for _ in range(N+1)]

for _ in range(M):
    u, v, w = map(int, input().split())
    graph[u][v] = w
    graph[v][u] = w

# container[x][y] = x에서 y노드를 최단경로를 통해 이동할 때, 제일 먼저 거쳐야 할 노드
container = [[i for i in range(N+1)] for _ in range(N+1)]

for k in range(1, N+1):
    graph[k][k] = 0
    container[k][k] = "-"
    for i in range(1, N+1):
        for j in range(1, N+1):
            new = graph[i][k] + graph[k][j]

            if new < graph[i][j]:
                graph[i][j] = new
                container[i][j] = container[i][k]

for i in range(1, N+1):
    print(*container[i][1:])