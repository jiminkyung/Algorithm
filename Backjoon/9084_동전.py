# 문제집 - 0x10강 - 다이나믹 프로그래밍


# 문제: https://www.acmicpc.net/problem/9084
# 메모리: 33432KB / 시간: 64ms
from sys import stdin


input = stdin.readline

T = int(input())
for _ in range(T):
    N = int(input())
    coins = list(map(int, input().split()))
    M = int(input())

    # dp[i] = i원을 만들 수 있는 경우의 수
    dp = [0] * (M+1)
    dp[0] = 1

    for coin in coins:
        # i가 coin 이상일 경우에만
        for i in range(coin, M+1):
            dp[i] += dp[i-coin]
            # coin = [1, 2]일때 5원을 만들 수 있는 경우는 아래와 같다.
            # 1) 5 - 1 = 4. 4원을 만든 후 5원으로 만들기
            # 2) 5 - 2 = 3. 3원을 만든 후 5원으로 만들기
            # 즉 dp[5] = dp[4] + dp[3] 과 같다.

    print(dp[M])