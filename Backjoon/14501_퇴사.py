# 문제집 - 0x10강 - 다이나믹 프로그래밍


# 문제: https://www.acmicpc.net/problem/14501
# 메모리: 31120KB / 시간: 40ms
from sys import stdin


input = stdin.readline

N = int(input())
lst = [list(map(int, input().split())) for _ in range(N)]
# dp[i] = i번째 원소를 포함하는 값 중 최대값
dp = [0] * N

# 첫째날 상담의 소요기간이 N일 이하일때만 예약 가능.
if lst[0][0] <= N:
    dp[0] = lst[0][1]

for i in range(1, N):
    # (현재 날짜 i + i일 상담의 소요기간 > 마지막 근무날 N) 이면 쓰루.
    if i + lst[i][0] > N:
        continue
    for j in range(i):
        # (현재 날짜 - j일 < j일 상담의 소요기간)이라면 dp[i]와 현재 날짜의 상담 보수 중 더 큰것을 택함.
        if (i - j) < lst[j][0]:
            dp[i] = max(dp[i], lst[i][1])
        else:
            dp[i] = max(dp[i], dp[j] + lst[i][1])

print(max(dp))