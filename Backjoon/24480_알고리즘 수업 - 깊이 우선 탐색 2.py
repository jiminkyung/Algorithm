# 그래프와 순회

# 내림차순으로 방문해야함
# 메모리: 67996KB / 시간: 560ms

import sys


sys.setrecursionlimit(10**6)  # 재귀 깊이 제한 증가
input = sys.stdin.readline
N, M, R = map(int, input().split())
graph = [[] for _ in range(N+1)]

for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

for i in range(1, N+1):
    graph[i].sort(reverse=True)  # 내림차순으로 방문하기때문에 reverse=True

visited = [0] * (N+1)
order = 1

def dfs(r: int):
    global order
    visited[r] = order
    order += 1

    for v in graph[r]:
        if not visited[v]:
            dfs(v)

dfs(R)

print(*visited[1:], sep="\n")


# 스택으로 풀면 재귀 제한을 따로 풀어줄 필요가 없다.
# 메모리: 60760KB / 시간: 488ms
from sys import stdin


input = stdin.readline
N, M, R = map(int, input().split())
graph = [[] for _ in range(N+1)]

for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

for i in range(1, N+1):
    graph[i].sort()  # 오름차순 형태로 스택에 추가하면 내림차순 형태로 꺼낼 수 있음.

visited = [0] * (N+1)

def dfs(r: int):
    order = 1
    stack = [r]
    
    while stack:
        node = stack.pop()
        if not visited[node]:
            visited[node] = order
            order += 1
            for v in graph[node]:
                if not visited[v]:
                    stack.append(v)

dfs(R)

print(*visited[1:], sep="\n")