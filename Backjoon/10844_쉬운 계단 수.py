# 동적 계획법 1
# 메모리: 31252KB / 시간: 40ms

"""
dp[i][j]: i자리 숫자이고 마지막 숫자(오른쪽)가 j인 계단 수의 경우
- 메모리 효율을 위해 자리가 0인 경우는 제외함. 따라서 i+1 자리 숫자가 됨.
- dp[0] -> 1자리 숫자, dp[1] -> 2자리 숫자...

0일경우 이전 숫자는 1만 가능.
9일경우 이전 숫자는 8만 가능.
"""

N = int(input())

dp = [[0]*10 for _ in range(N)]

for i in range(1, 10):
    dp[0][i] = 1

for i in range(1, N):
    for j in range(10):
        if j == 0:
            dp[i][j] = dp[i-1][1]
        elif j == 9:
            dp[i][j] = dp[i-1][8]
        else:
            dp[i][j] = dp[i-1][j-1] + dp[i-1][j+1]

print(sum(dp[N-1]) % 1000000000)