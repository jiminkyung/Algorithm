# 문제집 - BOJ 길라잡이 베타 (1)


# 문제: https://www.acmicpc.net/problem/11052

# dp[n] = 선택한 카드 갯수가 n개일때의 최대 비용
# 메모리: 31120KB / 시간: 212ms
from sys import stdin


input = stdin.readline

N = int(input())
cards = [0] + list(map(int, input().split()))

dp = [0] * (N+1)

for i in range(1, N+1):
    for j in range(1, i+1):
        dp[i] = max(dp[i], cards[j] + dp[i-j])

print(dp[N])