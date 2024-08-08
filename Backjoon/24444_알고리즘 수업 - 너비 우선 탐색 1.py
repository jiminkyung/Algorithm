# 그래프와 순회

# 깊스너큐! 깊이우선은 스택, 너비우선은 큐.
# 메모리: 60628KB / 시간: 560ms

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
    graph[i].sort()  # 큐는 선입선출(FIFO)이므로 그대로 오름차순 정렬.

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