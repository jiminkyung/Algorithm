# 문제집 - 0x10강 - 다이나믹 프로그래밍


# 문제: https://www.acmicpc.net/problem/1788
"""
f(-1) = 1
f(-2) = -1
f(-3) = 2

f(-2) = f(-3) + f(-4)
-1 = 2 + f(-4)
f(-4) = -3

f(-3) = f(-4) + f(-5)
2 = -3 + f(-5)
f(-5) = 5

-n이 짝수라면 -f(n), 홀수라면 f(n)
"""
# 메모리: 71968KB / 시간: 356ms
from sys import stdin


input = stdin.readline
MOD = 1000000000

N = int(input())

dp = [0, 1, 1] + [0] * (abs(N)-2)
dp[1] = dp[2] = 1

for i in range(3, abs(N)+1):
    dp[i] = (dp[i-1] + dp[i-2]) % MOD

# N이 음수, 짝수면 -F(N)
if N < 0 and N % 2 == 0:
    print(-1)
elif N == 0:
    print(0)
else:
    print(1)

print(dp[abs(N)])