# 문제집 - 0x1A강 - 위상 정렬


# 문제: https://www.acmicpc.net/problem/2056

# ⭐ DP + BFS 문제
# 메모리: 39632KB / 시간: 332ms
from sys import stdin
from collections import deque


input = stdin.readline

N = int(input())
graph = [[] for _ in range(N+1)]
in_degree = [0] * (N+1)
time = [0] * (N+1)  # 각 작업들의 소요시간

for i in range(1, N+1):
    t, m, *nodes = map(int, input().split())

    time[i] = t
    if m != 0:
        in_degree[i] += m  # 현재 노드의 진입차수 기록

        for node in nodes:
            graph[node].append(i)  # 선행노드 -> 현재노드로 연결될 수 있게 저장


def bfs() -> int:
    queue = deque()
    dp = [0] * (N+1)  # dp[x] = x작업까지 마치는데에 걸리는 최대 소요시간

    for i in range(1, N+1):
        # 진입차수가 0인 작업들을 큐에 넣어주고 dp 업데이트
        if in_degree[i] == 0:
            queue.append(i)
            dp[i] = time[i]
    
    while queue:
        curr = queue.popleft()

        for node in graph[curr]:
            in_degree[node] -= 1
            
            # 선행작업 후 현재작업을 수행하는데에 걸리는 시간
            # 이전 선행작업 중 가장 많이 소요되는 작업이 끝난 후에 현재 작업을 시작할 수 있음.
            dp[node] = max(dp[node], dp[curr] + time[node])

            if in_degree[node] == 0:
                queue.append(node)
    return max(dp)


print(bfs())