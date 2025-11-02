# 다이나믹 프로그래밍


# 문제: https://www.acmicpc.net/problem/2688

# 기본적인 DP 문제. 나중에 DP 연습할때 풀어봐도 좋을듯.
# 메모리: 32412KB / 시간: 32ms
from sys import stdin


input = stdin.readline

def main():
    T = int(input())

    # n은 최대 64
    dp = [[0] * 10 for _ in range(65)]
    
    # 한자릿수의 경우 줄어들지 않는 수는 i 하나뿐.
    for i in range(10):
        dp[1][i] = 1
    
    # dp[i][j]: i자리 수 중에서 마지막이 j인 수의 값
    for i in range(2, 65):
        for j in range(10):
            # 왼쪽 <= 오른쪽 이어야 하므로, j의 앞자리 수는 j보다 작거나 같아야 함.
            # dp[i][j-1]: 마지막 숫자가 j보다 작은 경우들
            # dp[i-1][j]: 마지막 숫자가 j인 i-1자리 수들에 j를 붙인 경우
            # 위 값을 더해주면 dp[i][j]값이 됨.
            dp[i][j] = dp[i][j-1] + dp[i-1][j]
    
    for _ in range(T):
        n = int(input())
        print(sum(dp[n]))


main()