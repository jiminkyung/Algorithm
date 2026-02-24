# 다이나믹 프로그래밍
# 임의 정밀도 / 큰 수 연산


# 문제: https://www.acmicpc.net/problem/3372

# 기본적인 DP문제
# 메모리: 33432KB / 시간: 44ms
from sys import stdin


input = stdin.readline

def main():
    N = int(input())
    dp = [[0] * N for _ in range(N)]

    # 오른쪽과 아래쪽만 가능
    dx = [1, 0]
    dy = [0, 1]

    arr = [tuple(map(int, input().split())) for _ in range(N)]

    # dp[i][j]: (i, j)좌표까지 도달할 수 있는 경우의 수
    dp[0][0] = 1

    for x in range(N):
        for y in range(N):
            size = arr[x][y]

            # 만약 현재 위치값이 0이면 멈추기
            if not size:
                continue

            # 오른쪽, 아래로만 움직일 수 있음.
            for i in range(2):
                nx = x + dx[i] * size
                ny = y + dy[i] * size

                if not (0 <= nx < N and 0 <= ny < N):
                    continue

                # 새로운 좌표의 경우의 값에 현재 위치의 경우의 값을 더해줌.
                dp[nx][ny] += dp[x][y]
    
    print(dp[N-1][N-1])


main()