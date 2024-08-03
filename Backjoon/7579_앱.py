# 동적 계획법 2

# 메모리: 48056KB / 시간: 636ms

from sys import stdin


input = stdin.readline
N, M = map(int, input().split())

memories = list(map(int, input().split()))
costs = list(map(int, input().split()))

dp = [[0]*(sum(costs) + 1) for _ in range(N+1)]

ret = float("inf")

for i in range(1, N+1):
    for j in range(sum(costs) + 1):
        if j < costs[i-1]:  # 현재 비용으로 i번째 앱을 비활성화할 수 없는 경우
            dp[i][j] = dp[i-1][j]  # 이전 상태 그대로 유지
        else:  # 현재 비용으로 i번째 앱을 비활성화할 수 있는 경우
            dp[i][j] = max(dp[i-1][j-costs[i-1]] + memories[i-1], dp[i-1][j])  # 비활성화하는 경우와 하지 않는 경우 중 최대값 선택
        
        if dp[i][j] >= M:  # 필요한 메모리를 확보한 경우
            ret = min(ret, j)  # 최소 비용 갱신

print(ret)