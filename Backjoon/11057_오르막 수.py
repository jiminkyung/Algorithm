# 문제집 - 0x10강 - 다이나믹 프로그래밍


# 문제: https://www.acmicpc.net/problem/11057
# 메모리: 33432KB / 시간: 40ms
from sys import stdin


input = stdin.readline

N = int(input())
MOD = 10007

# dp[i][j] = 길이가 i인 오르막수 중 마지막 숫자가 j인 경우
dp = [[0] * 10 for _ in range(N+1)]

for j in range(10):
    dp[1][j] = 1

for i in range(2, N+1):
    for j in range(10):
        # j로 끝나는 i자리 오르막수의 경우 = 0~j-1로 끝나는 i-1자리 오르막수의 경우의 합
        dp[i][j] = sum(dp[i-1][:j+1]) % MOD

print(sum(dp[N]) % MOD)