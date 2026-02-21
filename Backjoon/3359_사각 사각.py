# 다이나믹 프로그래밍


# 문제: https://www.acmicpc.net/problem/3359

# 기본적인 DP문제
# 메모리: 33432KB / 시간: 36ms
from sys import stdin


input = stdin.readline

def main():
    N = int(input())
    rect = [tuple(map(int, input().split())) for _ in range(N)]

    dp = [[0, 0] for _ in range(N)]

    # dp[i][0]: i번째 사각형의 높이를 a로 결정했을 때.
    # dp[i][1]: i번째 사각형의 높이를 b로 결정했을 때.

    # 처음엔 높이 계산을 하지 않으므로 밑변의 길이만 더해줌.
    dp[0][0] = rect[0][1]  # 높이 a일때 밑변의 길이 b
    dp[0][1] = rect[0][0]  # 높이 b일때 밑변의 길이 a

    for i in range(1, N):
        a, b = rect[i]
        pa, pb = rect[i-1]

        # 변의 길이는 항상 a < b 임.
        # (현재까지의 합 + 이전 사각형과의 높이 차 + 현재 밑변 길이)
        # 높이를 a로 지정했을때 = 이전 높이 pa일때 / pb일때
        # 높이를 b로 지정했을때 = 이전 높이 pa일때 / pb일때
        # 크게 두가지, 총 네 가지 경우를 확인해야 함.

        # 1. 현재 높이를 a, 밑변을 b로 결정했을때.
        # 이전이 0번이었다면 -> pa가 높이 / 1번이었다면 -> pb가 높이.
        dp[i][0] = max(dp[i-1][0] + abs(a - pa) + b, dp[i-1][1] + abs(a - pb) + b)

        # 2. 현재 높이를 b, 밑변을 a로 결정했을때.
        # abs로 이전 높이 현재 높이 간극을 구하고, 현재 밑변 길이(b)를 더해주는거.
        dp[i][1] = max(dp[i-1][0] + abs(b - pa) + a, dp[i-1][1] + abs(b - pb) + a)
    
    print(max(dp[N-1]))


main()