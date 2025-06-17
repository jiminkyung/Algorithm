# 다이나믹 프로그래밍


# 문제: https://www.acmicpc.net/problem/1495
# 메모리: 32544KB / 시간: 48ms
from sys import stdin


input = stdin.readline

def main():
    N, S, M = map(int, input().split())
    V = [0] + list(map(int, input().split()))

    # dp[i][j]: i번째 곡을 연주하기 전에 볼륨을 j로 맞출 수 있는지
    # 볼륨 허용 범위: 0 <= x <= M
    dp = [[False] * (M+1) for _ in range(N+1)]
    dp[0][S] = True

    for song in range(1, N+1):
        for vol in range(M+1):
            if dp[song-1][vol]:  # 만약 이전 곡에서 vol까지 맞출 수 있었다면,
                if vol + V[song] <= M:  # +
                    dp[song][vol + V[song]] = True
                if vol - V[song] >= 0:  # -
                    dp[song][vol - V[song]] = True
    
    max_vol = -1

    # 볼륨이 큰 경우부터 거꾸로 순회
    for vol in range(M, -1, -1):
        if dp[N][vol]:
            max_vol = vol
            break
    
    print(max_vol)


main()