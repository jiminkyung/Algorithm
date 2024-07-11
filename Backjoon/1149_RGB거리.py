# 동적 계획법 1
# 메모리: 31120KB / 시간: 36ms

from sys import stdin


input = stdin.readline

N = int(input())

costs = [list(map(int, input().split())) for _ in range(N)]

def min_cost():
    dp = [costs[0]] + [[0, 0, 0] for _ in range(N-1)]

    for i in range(1, N):
        # 현재 집 색깔을 빨강으로 선택
        dp[i][0] = min(dp[i-1][1], dp[i-1][2]) + costs[i][0]
        # 초록으로
        dp[i][1] = min(dp[i-1][0], dp[i-1][2]) + costs[i][1]
        # 파랑으로
        dp[i][2] = min(dp[i-1][0], dp[i-1][1]) + costs[i][2]
    
    return min(dp[N-1])

print(min_cost())