# 문제집 - 0x18강 - 그래프


# 문제: https://www.acmicpc.net/problem/1325

# 모든 컴퓨터로 DFS / BFS 을 실행해야 함. Python3로 통과하기 힘들다.
# (PyPy3) 메모리: 210872KB / 시간: 10456ms
from sys import stdin
from collections import deque


input = stdin.readline

N, M = map(int, input().split())

graph = [[] for _ in range(N)]

for _ in range(M):
    A, B = map(int, input().split())
    graph[B-1].append(A-1)

def bfs(root):
    visited = [False] * N
    visited[root] = True
    queue = deque([root])
    cnt = 1

    while queue:
        node = queue.popleft()

        for nxt_node in graph[node]:
            if not visited[nxt_node]:
                cnt += 1
                visited[nxt_node] = True
                queue.append(nxt_node)
    return cnt


max_count = 0
ret = []

for i in range(N):
    curr_count = bfs(i)
    if curr_count > max_count:
        max_count = curr_count
        ret = [i+1]
    elif curr_count == max_count:
        ret.append(i+1)

print(*ret)