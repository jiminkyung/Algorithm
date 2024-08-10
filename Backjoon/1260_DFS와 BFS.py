# 그래프와 순회

# 메모리: 34112KB / 시간: 60ms

from sys import stdin
from collections import deque


input = stdin.readline
N, M, V = map(int, input().split())
graph = [[] for _ in range(N+1)]

for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

for i in range(1, N+1):
    graph[i].sort()

def dfs(v):
    visited = [False] * (N+1)
    ret = []
    stack = [v]

    while stack:
        node = stack.pop()
        if not visited[node]:
            visited[node] = True
            ret.append(node)
            for n in graph[node][::-1]:  # 스택은 후입선출이므로 역정렬 필요.
                if not visited[n]:
                    stack.append(n)

    return " ".join(map(str, ret))

def bfs(v):
    visited = [False] * (N+1)
    ret = []
    queue = deque([v])

    while queue:
        node = queue.popleft()
        if not visited[node]:
            visited[node] = True
            ret.append(node)
            for n in graph[node]:
                if not visited[n]:
                    queue.append(n)

    return " ".join(map(str, ret))

print(dfs(V), bfs(V), sep="\n")