# 문제집 - 0x10강 - 다이나믹 프로그래밍


# 문제: https://www.acmicpc.net/problem/9465
# 참고👉 https://great-park.tistory.com/101

# 메모리: 48120KB / 시간: 592ms
from sys import stdin


input = stdin.readline

T = int(input())

for _ in range(T):
    N = int(input())
    dp = [list(map(int, input().split())) for _ in range(2)]
    
    if N == 1:
        print(*max(dp))
    else:
        # (i, j) 스티커를 뜯는 경우 -> 대각선 위치의 스티커 or 그보다 한칸 옆의 스티커를 뜯어야함
        dp[0][1] += dp[1][0]
        dp[1][1] += dp[0][0]

        for i in range(2, N):
            dp[0][i] += max(dp[1][i-1], dp[1][i-2])
            dp[1][i] += max(dp[0][i-1], dp[0][i-2])
        
        print(max(dp[0][N-1], dp[1][N-1]))