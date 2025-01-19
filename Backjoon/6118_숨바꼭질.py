# 문제집 - 0x18강 - 그래프


# 문제: https://www.acmicpc.net/problem/6118
# 메모리: 39628KB / 시간: 136ms
from sys import stdin
from collections import deque


input = stdin.readline

N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]

for _ in range(M):
    A, B = map(int, input().split())
    graph[A].append(B)
    graph[B].append(A)


def bfs():
    queue = deque([(1, 0)])
    visited = [False] * (N+1)
    visited[1] = True
    
    max_dis = 0
    barn = 0  # 숨어야하는 헛간
    same = 0


    while queue:
        node, dis = queue.popleft()
        
        # 최대거리보다 dis가 크다면 업데이트
        if max_dis < dis:
            max_dis = dis
            barn = node
            same = 1
        # 최대거리와 같다면 번호가 더 작은 헛간을 선택, 같은 거리인 헛간의 수 카운트
        elif max_dis == dis:
            barn = min(node, barn)
            same += 1

        for nxt_node in graph[node]:
            if not visited[nxt_node]:
                visited[nxt_node] = True
                queue.append((nxt_node, dis+1))
    
    print(barn, max_dis, same)


bfs()