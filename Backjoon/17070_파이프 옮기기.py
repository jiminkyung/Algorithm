# 문제집 - 0x0D강 - 시뮬레이션


# 문제: https://www.acmicpc.net/problem/17070

# 사실상 DP 문제다.
# 메모리: 32544KB / 시간: 36ms
from sys import stdin


input = stdin.readline

N = int(input())
house = [list(map(int, input().split())) for _ in range(N)]

dp = [[[0] * 3 for _ in range(N)] for _ in range(N)]
dp[0][1][0] = 1  # 초기 상태: (0, 1) 가로 방향

for r in range(N):
    for c in range(N):
        if house[r][c] == 1:
            continue
        
        # 가로 방향
        if c > 0:
            dp[r][c][0] += dp[r][c - 1][0] + dp[r][c - 1][2]
        
        # 세로 방향
        if r > 0:
            dp[r][c][1] += dp[r - 1][c][1] + dp[r - 1][c][2]
        
        # 대각선 방향
        if r > 0 and c > 0 and house[r - 1][c] == 0 and house[r][c - 1] == 0:
            dp[r][c][2] += dp[r - 1][c - 1][0] + dp[r - 1][c - 1][1] + dp[r - 1][c - 1][2]

print(sum(dp[N - 1][N - 1]))