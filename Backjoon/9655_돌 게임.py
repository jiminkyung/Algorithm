# 문제집 - 0x10강 - 다이나믹 프로그래밍


# 문제: https://www.acmicpc.net/problem/9655
"""
1 - 상근
2 - 상근(1), 창영
3 - 상근(1), 창영(1), 상근
4 - 상근(1), 창영 or 상근(3), 창영
5 - 상근(1), 창영(1), 상근 or 상근(1), 창영(3), 상근 or 상근(3), 창영(1), 상근

즉 돌의 갯수 N이 홀수라면 상근, 짝수라면 창영이 이기게 된다.
굳이 DP를 사용하지 않아도 되는 문제다.
"""

# 1. DP 사용 없이 홀/짝으로 판별
# 메모리: 32544KB / 시간: 36ms
from sys import stdin


input = stdin.readline

N = int(input())
print("SK" if N % 2 != 0 else "CY")


# 2. DP 사용
# 메모리: 32544KB / 시간: 40ms
from sys import stdin


input = stdin.readline

N = int(input())
# dp[i] = 돌이 i개 남았을때, 현재 차례인 사람(상근)이 이길 수 있는지
dp = [False] * (N+1)

# True: 현재 차례가 승리 == 상근, False: 현재 차례가 패배 == 창영
dp[1] = True
if N > 1:
    dp[2] = False
if N > 2:
    dp[3] = True

for i in range(4, N+1):
    # dp[i-1], dp[i-3] => 상대방이 i-1, i-3개의 돌에서 승리할 가능성
    # 즉 현재 차례인 사람이 1개나 3개를 가져갔을때, 상대방은 패배 상태여야함.
    dp[i] = not dp[i-1] or not dp[i-3]

print("SK" if dp[N] else "CY")