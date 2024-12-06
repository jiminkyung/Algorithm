# 문제집 - 0x10강 - 다이나믹 프로그래밍


# 문제: https://www.acmicpc.net/problem/11055
# 11053_가장 긴 증가하는 부분수열 과 비슷한 문제다.

# 메모리: 31120KB / 시간: 204KB
from sys import stdin


input = stdin.readline

N = int(input())
A = list(map(int, input().split()))

dp = [0] * N
dp[0] = A[0]

for i in range(1, N):
    for j in range(i):
        if A[i] > A[j]:
            dp[i] = max(dp[i], dp[j] + A[i])
        else:  # A[i] < A[j]
            dp[i] = max(dp[i], A[i])

print(max(dp))