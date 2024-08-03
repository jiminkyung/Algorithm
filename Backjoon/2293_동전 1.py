# 동적 계획법 2

# 메모리: 31120KB / 시간: 168ms

from sys import stdin


input = stdin.readline
n, k = map(int, input().split())

coins = sorted(int(input()) for _ in range(n))
# 정렬하지 않아도 된다.
# coins = [int(input()) for _ in range(n)] 으로 변경 시 148ms

dp = [1] + [0]*k  # dp[0]은 1로 설정해둬야 함.(dp[가치]일때 가치 = 해당 동전 일 경우)

for coin in coins:
    for i in range(coin, k+1):
        dp[i] += dp[i - coin]

print(dp[k])