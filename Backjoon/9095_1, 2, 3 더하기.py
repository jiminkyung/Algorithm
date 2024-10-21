# 문제집 - BOJ 길라잡이 베타 (1)


# 문제: https://www.acmicpc.net/problem/9095
# 4 = 1+dp[3], 2+dp[2], 3+dp[1], 5 = 1+dp[4], 2+dp[3], 3+dp[2]

# 메모리: 31120KB / 시간: 32ms
from sys import stdin


input = stdin.readline

dp = [0] * 11
dp[1] = 1
dp[2] = 2
dp[3] = 4

for i in range(4, 11):
    dp[i] = dp[i-1] + dp[i-2] + dp[i-3]

T = int(input())

for _ in range(T):
    print(dp[int(input())])