# 문제집 - 0x1A강 - 위상 정렬


# 문제: https://www.acmicpc.net/problem/1005

# 2056_작업 과 비슷한 문제. DP + BFS를 사용한다.
# 메모리: 37616KB / 시간: 968ms
from sys import stdin
from collections import deque


input = stdin.readline

def bfs():
    dp = [0] * (N+1)
    queue = deque()

    for i in range(1, N+1):
        if in_degree[i] == 0:
            queue.append(i)
            dp[i] = time[i]
    
    while queue:
        curr = queue.popleft()

        for node in graph[curr]:
            in_degree[node] -= 1
            # 현재 건물을 짓는 최소시간 = 기존값 or 이전 건물을 짓는 최소시간 + 현재 건물을 짓는 시간
            dp[node] = max(dp[node], dp[curr] + time[node])

            if in_degree[node] == 0:
                queue.append(node)
    return dp[W]  # W 건물을 짓는데까지 소요되는 최소 시간


T = int(input())

for _ in range(T):
    N, K = map(int, input().split())
    graph = [[] for _ in range(N+1)]
    in_degree = [0] * (N+1)
    time = [0] + list(map(int, input().split()))  # 건물을 짓는데 걸리는 시간

    for _ in range(K):
        X, Y = map(int, input().split())  # X를 지어야 Y를 지을 수 있음
        graph[X].append(Y)
        in_degree[Y] += 1
    
    W = int(input())  # 타겟 건물
    print(bfs())