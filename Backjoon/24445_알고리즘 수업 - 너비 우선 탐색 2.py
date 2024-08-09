# 그래프와 순회

# 메모리: 60992KB / 시간: 536ms

from sys import stdin
from collections import deque


input = stdin.readline
N, M, R = map(int, input().split())
graph = [[] for _ in range(N+1)]
visited = [0] * (N+1)

for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

for i in range(1, N+1):
    graph[i].sort(reverse=True)  # 내림차순으로 정렬

def bfs(r: int):
    queue = deque([r])
    order = 1

    while queue:
        node = queue.popleft()
        if not visited[node]:
            visited[node] = order
            order += 1
            for v in graph[node]:
                if not visited[v]:
                    queue.append(v)

bfs(R)

print(*visited[1:], sep="\n")