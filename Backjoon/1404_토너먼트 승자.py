# 수학
# 구현
# 확률론
# 브루트포스 알고리즘


# 문제: https://www.acmicpc.net/problem/1404
# 메모리: 32412KB / 시간: 36ms
from sys import stdin


input = stdin.readline

def main():
    # odds[a][b]: a가 b를 이길 확률
    odds = [[0.0]*8 for _ in range(8)]
    data = list(map(int, input().split()))

    # 매 턴마다 data의 인덱스를 증가시킴
    # 또는 등차수열 공식을 사용해서 idx = i*(15 - i)//2 + (j-i-1) 로 계산해도 됨. (40ms)
    # => i번이 가진 데이터 갯수는 7-i개. i번 이전까지의 데이터 갯수: 7부터 7-(i-1)까지의 등차수열 합.
    # => 즉, i * (7 + (8-i)) // 2개. i번의 데이터 내에서 j번 참가자의 위치는 j-i-1.
    idx = 0
    for i in range(8):
        for j in range(i+1, 8):
            per = data[idx] / 100.0  # 백분률로 변환시킨 후 할당
            odds[i][j] = per
            odds[j][i] = 1 - per
            idx += 1
    
    # dp[x][a]: x라운드에 a가 우승할 확률
    # dp[0] ~ dp[2]까지 1라운드 ~ 3라운드 결과 저장
    dp = [[0.0]*8 for _ in range(3)]

    # 1라운드 (0,1 / 2,3 / 4,5 / 6,7)
    for i in range(0, 8, 2):
        a, b = i, i+1
        dp[0][a] = odds[a][b]
        dp[0][b] = odds[b][a]
    
    # 2라운드 (0,1 <-> 2,3 / 4,5 <-> 6,7)
    for i in range(2):
        group = [4*i+j for j in range(4)]
        for p1 in group[:2]:
            for p2 in group[2:]:
                dp[1][p1] += dp[0][p1] * dp[0][p2] * odds[p1][p2]
                dp[1][p2] += dp[0][p1] * dp[0][p2] * odds[p2][p1]
    
    # 3라운드 (0,1,2,3 <-> 4,5,6,7)
    for p1 in range(4):
        for p2 in range(4, 8):
            dp[2][p1] += dp[1][p1] * dp[1][p2] * odds[p1][p2]
            dp[2][p2] += dp[1][p1] * dp[1][p2] * odds[p2][p1]
    
    for i in range(8):
        print(f"{dp[2][i]:.10f}", end=" ")


main()