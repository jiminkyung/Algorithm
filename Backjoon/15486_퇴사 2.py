# 문제집 - 0x10강 - 다이나믹 프로그래밍


# 문제: https://www.acmicpc.net/problem/15486
# 역순으로 풀어야 중복 체크 없이 한번에 가능!

# ⭐ 1. dp를 N+1만큼 생성. 직관적인 코드.
# 시간 단축 요인: 튜플 사용, (time, pay)와 같이 언패킹
# 메모리: 252484KB / 시간: 2044ms
from sys import stdin


input = stdin.readline

N = int(input())
lst = [tuple(map(int, input().split())) for _ in range(N)]

dp = [0] * (N + 1)

for i in range(N - 1, -1, -1):  # 역순으로 순회
    time, pay = lst[i]
    if i + time > N:  # 상담 종료일이 퇴사일 이후
        dp[i] = dp[i + 1]
    else:
        # 현재 상담을 수행하는 경우와 수행하지 않는 경우 중 최댓값
        dp[i] = max(dp[i + 1], pay + dp[i + time])

print(dp[0])


# 2. dp를 N만큼 생성.
# 메모리: 253508KB / 시간: 2220ms
from sys import stdin


input = stdin.readline

N = int(input())
lst = [tuple(map(int, input().split())) for _ in range(N)]

dp = [0] * N

if lst[N-1][0] == 1:
    dp[N-1] = lst[N-1][1]

for i in range(N-2, -1, -1):  # 역순으로 순회
    time, pay = lst[i]
    if i + time > N:  # 상담 종료일이 퇴사일 이후
        dp[i] = dp[i + 1]
    else:
        # 현재 상담을 수행하는 경우와 수행하지 않는 경우 중 최댓값
        dp[i] = max(dp[i+1] if i+1 < N else 0, pay + (dp[i+time] if i+time < N else 0))

print(dp[0])