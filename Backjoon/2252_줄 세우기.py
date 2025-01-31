# 문제집 - 0x1A강 - 위상 정렬


# 문제: https://www.acmicpc.net/problem/2252

# 위상정렬(Topological Sorting): DAG(방향 사이클이 없는 방향 그래프)의 노드들을 순서화
# BFS, DFS 모두 사용 가능. 단방향으로 저장한다.

# 1. DFS 사용
# 진입차수(in-degree) 불필요
# 메모리: 39328KB / 시간: 156ms
from sys import stdin


input = stdin.readline

N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]

for _ in range(M):
    u, v = map(int, input().split())

    graph[u].append(v)


def dfs():
    stack = []
    visited = [False] * (N+1)
    ret = []

    for i in range(1, N+1):
        if visited[i]:
            continue

        stack.append((i, False))

        while stack:
            curr, is_done = stack.pop()  # (현재 노드, 후처리 여부)

            if is_done:  # ✅ 후처리 단계 - 자식 노드를 모두 방문 후 본인 노드 처리
                ret.append(curr)
                continue

            if visited[curr]:  # 이미 방문한 노드면 무시
                continue

            visited[curr] = True  # 현재 노드 방문처리, 후처리를 위해 다시 push
            stack.append((curr, True))

            for node in graph[curr]:
                if not visited[node]:
                    stack.append((node, False))
    return ret[::-1]  # 뒤집어서 반환


print(*dfs())

# 🚨 중간에 if visited[curr] 조건이 없다면 틀림.
# 반례는 아래와 같다.
"""
3 3
1 3
2 3
1 2
답: 1 2 3
결과: 1 3 2 3
"""


# 2. BFS 사용
# 진입차수(in-degree)로 체크
# 메모리: 40908KB / 시간: 188ms
from sys import stdin
from collections import deque


input = stdin.readline

N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]
degree = [0] * (N+1)

for _ in range(M):
    u, v = map(int, input().split())

    degree[v] += 1
    graph[u].append(v)

queue = deque()
visited = [False] * (N+1)
ret = []

for i in range(1, N+1):
    if not degree[i]:
        queue.append(i)
        visited[i] = True

def bfs():
    while queue:
        curr = queue.popleft()
        ret.append(curr)

        for node in graph[curr]:
            if not visited[node]:
                degree[node] -= 1
                if degree[node] == 0:
                    queue.append(node)
                    visited[node] = True

bfs()
print(*ret)


# 3. 재귀를 사용한 DFS 방식
# is_done 같은 체크 변수 필요 X
# 메모리: 39580KB / 시간: 156ms
from sys import stdin


input = stdin.readline

N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]

for _ in range(M):
    u, v = map(int, input().split())

    graph[u].append(v)


visited = [False] * (N+1)
ret = []

def dfs(curr):
    visited[curr] = True
    for node in graph[curr]:
        if not visited[node]:
            dfs(node)
    
    ret.append(curr)


for i in range(1, N+1):
    if not visited[i]:
        dfs(i)


print(*ret[::-1])