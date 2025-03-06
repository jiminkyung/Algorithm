# 문제집 - 0x1D강 - 다익스트라 알고리즘


# 문제: https://www.acmicpc.net/problem/1162

# "K > 경로상 도로의 갯수" 일 경우를 주의해야함!
# 반례👉 https://www.acmicpc.net/board/view/135692

# 다시 풀어볼만한 문제.
# 메모리: 56676KB / 시간: 892ms
from sys import stdin
from heapq import heappush, heappop


input = stdin.readline
INF = float("inf")

N, M, K = map(int, input().split())
graph = [[] for _ in range(N+1)]

for _ in range(M):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))
    graph[v].append((u, w))


def dijkstra():
    # 2차원 dp로 구해보자.
    # dp[k][i]: 도로를 k개까지 포장했을때 i번 도시까지 가는 최소시간
    dp = [[INF] * (N+1) for _ in range(K+1)]
    dp[0][1] = 0
    heap = [(0, 1, 0)]  # 시간, 지역, 포장횟수

    while heap:
        time, curr, cnt = heappop(heap)

        if dp[cnt][curr] < time:
            continue

        for nxt, t in graph[curr]:
            new_time = time + t
            # 1. 도로 포장 X
            if new_time < dp[cnt][nxt]:
                dp[cnt][nxt] = new_time
                heappush(heap, (new_time, nxt, cnt))
            # 2. 도로 포장 O
            if cnt < K and time < dp[cnt+1][nxt]:
                dp[cnt+1][nxt] = time
                heappush(heap, (time, nxt, cnt+1))
    
    return min(dp[i][N] for i in range(K+1))
    # 🚨 단순히 dp[K][N]만 반환하면 X. 최적경로의 도로 갯수가 K보다 작을 경우 부정확한 값이 저장됨.


print(dijkstra())