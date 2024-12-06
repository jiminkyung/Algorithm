# 문제집 - 0x10강 - 다이나믹 프로그래밍


# 문제: https://www.acmicpc.net/problem/15486
# 역순으로 풀어야 중복 체크 없이 한번에 가능

# 메모리: 346424KB / 시간: 2832ms
from sys import stdin


input = stdin.readline

N = int(input())
lst = [list(map(int, input().split())) for _ in range(N)]
dp = [0] * (N+1)

c = 0
for i in range(N):
    c = max(dp[i], c)
    if lst[i][0] <= N - i:
        dp[i + lst[i][0]] = max(c + lst[i][1], dp[i + lst[i][0]])

print(max(dp))