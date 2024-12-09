# 문제집 - 0x10강 - 다이나믹 프로그래밍


# 문제: https://www.acmicpc.net/problem/2302
# 메모리: 32412KB / 시간: 32ms
from sys import stdin


input = stdin.readline

N = int(input())
M = int(input())

vip = [int(input()) for _ in range(M)]
dp = [0] * (N+1)

dp[0] = dp[1] = 1

if N > 1:
    dp[2] = 2

# dp[i-1]: i번 좌석에 앉았을때의 경우의 수
# dp[i-2]: i-1번 좌석에 앉았을때의 경우의 수
for i in range(3, N+1):
    dp[i] = dp[i-1] + dp[i-2]

ret = 1
tmp = 0

# 만약 M이 1 이상이라면 vip 사이 구간들의 길이를 구한 뒤 해당 dp값을 곱해준다.
# N = 9, M = [4, 7]일때,
# [1, 2, 3]: dp[3] / [5, 6]: dp[2] / [8, 9]: dp[2]
# => dp[3] * dp[2] * dp[2]
if vip:
    for v in vip:
        ret *= dp[v-1-tmp]
        tmp = v
    ret *= dp[N-tmp]  # 마지막 vip 좌석 이후의 구간
else:
    ret = dp[N]

print(ret)