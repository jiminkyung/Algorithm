# 동적 계획법 2

# 메모리: 42756KB / 시간: 136ms => (재채점) 메모리: 44120KB / 시간: 108ms

import sys


sys.setrecursionlimit(10**9)  # 재귀 깊이를 늘려줘야 함
input = sys.stdin.readline

M, N = map(int, input().split())
boards = [tuple(map(int, input().split())) for _ in range(M)]

dx = (-1, 1, 0, 0)
dy = (0, 0, -1, 1)

dp = [[-1]*N for _ in range(M)]

def dfs(x, y):
    # 목적지 도달 시
    if x == M-1 and y == N-1:
        return 1
    
    # 이미 계산된 결과가 있다면 그 값을 반환(메모이제이션)
    if dp[x][y] != -1:
        return dp[x][y]
    
    dp[x][y] = 0
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < M and 0 <= ny < N and boards[nx][ny] < boards[x][y]:
            dp[x][y] += dfs(nx, ny)
    
    return dp[x][y]

print(dfs(0, 0))