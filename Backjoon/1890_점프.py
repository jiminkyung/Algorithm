# 다이나믹 프로그래밍


# 문제: https://www.acmicpc.net/problem/1890

# DP 문제다. DP 연습할때 다시 풀어볼만한 문제.
# 메모리: 32412KB / 시간: 32ms
from sys import stdin


input = stdin.readline

def main():
    N = int(input())
    field = [list(map(int, input().split())) for _ in range(N)]

    # dp[i][j]: (i, j)까지 갈 수 있는 방법의 수
    dp = [[0] * N for _ in range(N)]
    dp[0][0] = 1

    for i in range(N):
        for j in range(N):
            k = field[i][j]

            # dp값이 0이거나, k가 0이라면 넘어감
            if dp[i][j] == 0 or k == 0:
                continue
            # 오른쪽 or 아래로만 이동 가능
            for nx, ny in ((i+k, j), (i, j+k)):
                if 0 <= nx < N and 0 <= ny < N:
                    # 경우의 수를 더해준다.
                    # -> 각 경로는 독립적이므로 곱하면 X, 더해야 함.
                    dp[nx][ny] += dp[i][j]
    
    print(dp[N-1][N-1])


main()