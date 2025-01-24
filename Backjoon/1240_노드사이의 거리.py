# 문제집 - 0x19강 - 트리


# 문제: https://www.acmicpc.net/problem/1240

# ! 플로이드-워셜로 풀면 시간초과
# 메모리: 33432KB / 시간: 168ms
from sys import stdin


input = stdin.readline

N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]

for _ in range(N-1):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))
    graph[v].append((u, w))

def bfs(a, b):
    visited = [False] * (N+1)
    visited[a] = True
    curr = [(a, 0)]  # (노드, 거리) 저장

    while curr:
        nxt = []
        for cur_node, dis in curr:
            if cur_node == b:
                return dis
            for nxt_node, new_dis in graph[cur_node]:
                if not visited[nxt_node]:
                    visited[nxt_node] = True
                    nxt.append((nxt_node, dis + new_dis))  # (다음 노드, 현재까지의 거리 + 새로운 거리)
        curr = nxt


for _ in range(M):
    a, b = map(int, input().split())
    print(bfs(a, b))