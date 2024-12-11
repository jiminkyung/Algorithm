# 문제집 - 0x10강 - 다이나믹 프로그래밍


# 문제: https://www.acmicpc.net/problem/9657
# 메모리: 32544KB / 시간: 44ms
from sys import stdin


input = stdin.readline

N = int(input())

dp = [False] * 1001
dp[1] = dp[3] = dp[4] = True

# 현재 플레이어가 이기려면 = -1개 or -3개 or -4개를 가져가고 난 후, 상대 플레이어가 지는 상황이어야 함.
for i in range(5, 1001):
    dp[i] = not dp[i-1] or not dp[i-3] or not dp[i-4]

print("SK" if dp[N] else "CY")