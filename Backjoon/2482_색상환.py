# 문제집 - 0x10강 - 다이나믹 프로그래밍


# 문제: https://www.acmicpc.net/problem/2482
# 메모리: 44872KB / 시간: 456ms
from sys import stdin


input = stdin.readline
MOD = 1000000003

N = int(input())
K = int(input())

"""
dp[i][j] = 1번부터 i번까지의 색 중에서 j개를 선택하는 경우의 수

[1, 2, 3, 4, 5]

4번까지의 색 중에서 2개를 선택해야 할 경우
1) 4번 색상을 고르지 않는다면
    [1, 2, 3] 중에서 2개의 색상을 고르면 됨
2) 4번 색상을 고른다면
    [1, 2] 중에서 1개의 색상을 고르면 됨
=> dp[4][2] = dp[3][2] + dp[2][1]
=> dp[i][j] = dp[i-1][j] + dp[i-2][j-1]

단, 5번까지의 색상 중에서 선택해야 할 경우는 따로 처리해야한다.
색상표가 원형으로 이루어져 있기 때문에 N개의 색상 중 N번째 색상을 선택한다면,
[1, 2, 3, 4, 5] 에서 가능한 색상은 [2, 3] 이 된다.
즉 i = 5, j = 2일때 5번 색상을 포함한다면,
=> dp[2][1]
=> dp[i-3][j-1]
"""

dp = [[0] * (K+1) for _ in range(N+1)]

for i in range(N+1):
    for j in range(K+1):
        if j == 0:
            dp[i][j] = 1
            continue

        if j == 1:
            dp[i][j] = i
            continue

        # dp[0][j]는 어떻게 계산해도 0끼리 더하는 셈이므로 문제 없음.
        dp[i][j] += dp[i-1][j]
        dp[i][j] += dp[i-2][j-1] if i != N else dp[i-3][j-1]

        dp[i][j] %= MOD

print(dp[N][K])