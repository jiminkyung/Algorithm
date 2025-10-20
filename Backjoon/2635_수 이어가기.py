# 수학
# 브루트포스 알고리즘


# 문제: https://www.acmicpc.net/problem/2635

# 2502_떡 먹는 호랑이와 비슷한 문제. DP 활용? 피보나치 수열과도 비슷함.
# 메모리: 33432KB / 시간: 44ms
from sys import stdin


input = stdin.readline

def main():
    N = int(input())

    # dp는 넉넉하게 1000으로 설정
    dp = [[0, 0] for _ in range(1000)]
    dp[0] = [1, 0]
    dp[1] = [0, 1]

    # dp[i] = [N 갯수, M 갯수]
    for i in range(2, 1000):
        dp[i][0] = dp[i-2][0] - dp[i-1][0]
        dp[i][1] = dp[i-2][1] - dp[i-1][1]
    
    # max_cnt: 최대 갯수, max_num: 최대 갯수일때의 M 값
    max_cnt = 2
    max_num = 0

    # 3번째 값 까지는 무조건 구할 수 있음. (1 1 이어도 1-1 = 0이니 1 1 0 가능)
    # 4번째 값의 식은 -N+2M. 이게 0 이상이어야 하니 -N+2M >= 0, 2M >= N, M >= N/2 가 된다.
    # 또한 M이 N보다 크면 3번째 값을 구할 수 없으므로 N 이하여야 함.
    for M in range(N//2 + 1, N + 1):
        for i in range(2, 1000):
            if dp[i][0] * N + dp[i][1] * M < 0:
                if max_cnt < i:
                    max_cnt = i
                    max_num = M
                break
    
    print(max_cnt)
    for i in range(max_cnt):
        print(dp[i][0] * N + dp[i][1] * max_num, end=" ")


main()