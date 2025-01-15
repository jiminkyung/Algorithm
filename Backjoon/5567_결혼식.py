# 문제집 - 0x18강 - 그래프


# 문제: https://www.acmicpc.net/problem/5567
# 메모리: 34924KB / 시간: 60ms
from sys import stdin
from collections import deque


input = stdin.readline

N = int(input())
M = int(input())

graph = [[] for _ in range(N+1)]

# 양방향으로 저장
for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)


def bfs():
    visited = [False] * (N+1)
    visited[1] = True
    queue = deque([(1, 2)])
    cnt = 0

    while queue:
        num, dis = queue.popleft()

        for friend in graph[num]:
            if not visited[friend] and dis > 0:  # 친구의 친구까지만 계산
                cnt += 1
                visited[friend] = True
                queue.append((friend, dis-1))
    
    return cnt


print(bfs())