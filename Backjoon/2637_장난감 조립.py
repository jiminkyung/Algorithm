# 문제집 - 0x1A강 - 위상 정렬


# 문제: https://www.acmicpc.net/problem/2637

# DP + BFS 문제
# 메모리: 34968KB / 시간: 56ms
from sys import stdin
from collections import deque


input = stdin.readline

N = int(input())
graph = [[] for _ in range(N+1)]
in_degree = [0] * (N+1)

M = int(input())
for _ in range(M):
    X, Y, K = map(int, input().split())
    # X를 만드려면 Y가 K개 필요함.
    # => 더 기본이 되는 부품이 먼저 만들어져야함.
    graph[Y].append((X, K))
    in_degree[X] += 1

queue = deque()
for i in range(1, N+1):
    if in_degree[i] == 0:
        queue.append(i)

# dp[x][y] = x를 만드는데 필요한 기본부품 y의 갯수
dp = [[0] * (N+1) for _ in range(N+1)]

def bfs():
    while queue:
        curr = queue.popleft()

        # nxt = curr을 cnt만큼 필요로 하는 부품
        for nxt, cnt in graph[curr]:
            # 필요한 부품이 0이라면 기본부품이라는 뜻
            if sum(dp[curr]) == 0:
                dp[nxt][curr] += cnt
            else:
                # 기본부품이 아닐경우, curr을 만드는데에 필요한 기본부품 i의 수 * cnt를 더해줌
                for i in range(1, N+1):
                    dp[nxt][i] += dp[curr][i] * cnt
            
            in_degree[nxt] -= 1
            if in_degree[nxt] == 0:
                queue.append(nxt)


bfs()
for i in range(1, N+1):
    if dp[N][i] > 0:
        print(i, dp[N][i])