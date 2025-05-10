# 다이나믹 프로그래밍


# 문제: https://www.acmicpc.net/problem/1309

# DP 문제.
# 메모리: 36264KB / 시간: 60ms
from sys import stdin


input = stdin.readline

def main():
    N = int(input())
    MOD = 9901

    dp = [0] * (N+1)
    dp[0] = 1  # 사자를 아예 배치하지 않을 경우
    dp[1] = 3  # 1x2 행렬에 사자를 배치하는 경우 = [0][0], [0][1]에 배치 + 배치 X

    # dp[i]의 값은 dp[i-1] + (dp[i-1] + dp[i-2]) 와 같다.
    # dp[2] = dp[1] + (dp[1] + dp[0]) = 3 + (3+1) = 7
    # dp[3] = dp[2] + (dp[2] + dp[1]) = 7 + (7+3) = 17 ...
    # => 즉 dp[i] = dp[i-1] * 2 + dp[i-2] 인 셈.
    for i in range(2, N+1):
        dp[i] = (dp[i-1] * 2 + dp[i-2]) % MOD
    
    print(dp[N])


main()