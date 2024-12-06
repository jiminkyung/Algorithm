# 문제집 - 0x10강 - 다이나믹 프로그래밍


# 문제: https://www.acmicpc.net/problem/2193
# 1, 10, 101 100, 1000 1001 1010, ... 피보나치 수열과 동일
# 메모리: 31120KB / 시간: 36ms
from sys import stdin


N = int(stdin.readline())

dp = [0] * (N+1)
dp[1] = 1

for i in range(2, N+1):
    dp[i] = dp[i-1] + dp[i-2]

print(dp[N])