# 자료 구조
# 브루트포스 알고리즘
# 누적 합
# 해시를 사용한 집합과 맵


# 문제: https://www.acmicpc.net/problem/1184

# 2차원 배열 누적합 사용. (2167_2차원 배열의 합 참고)
# 메모리: 32412KB / 시간: 1788ms
from sys import stdin


input = stdin.readline

def main():
    N = int(input())
    # 2차원 배열 누적합 계산을 위해 좌우로 0 깔아주기
    field = [[0] * (N+1)] + [[0] + list(map(int, input().split())) for _ in range(N)]
    
    # field[i][j]: (1, 1) ~ (i, j) 직사각형의 합
    for i in range(1, N+1):
        for j in range(1, N+1):
            field[i][j] += field[i-1][j] + field[i][j-1] - field[i-1][j-1]
    

    def calc(x1, y1, x2, y2):
        """ (x1, y1) ~ (x2, y2) 직사각형의 합 """
        val = field[x2][y2] - field[x1-1][y2] - field[x2][y1-1] + field[x1-1][y1-1]
        return val
    

    ret = 0

    # (x, y)를 경계선으로 삼아서 좌상-우하 / 우상-좌하 조합 탐색.
    # 경계선을 시작점/끝점으로 삼고 가능한 직사각형 합을 모두 체크,
    # 꼭짓점이 맞닿은 대각선 방향에 해당 합과 일치한 경우가 있다면 ret에 해당 경우의 갯수 추가.
    for x in range(1, N):
        for y in range(1, N):
            comb = {}
            
            # 1. 좌상 - 우하 조합
            # 좌상
            for i in range(1, x+1):
                for j in range(1, y+1):
                    val = calc(i, j, x, y)
                    comb[val] = comb.get(val, 0) + 1
            # 우하
            for i in range(x+1, N+1):
                for j in range(y+1, N+1):
                    val = calc(x+1, y+1, i, j)
                    ret += comb.get(val, 0)
            
            comb = {}

            # 2. 우상 - 좌하 조합
            # 우상
            for i in range(1, x+1):
                for j in range(y+1, N+1):
                    val = calc(i, y+1, x, j)
                    comb[val] = comb.get(val, 0) + 1
            # 좌하
            for i in range(x+1, N+1):
                for j in range(1, y+1):
                    val = calc(x+1, j, i, y)
                    ret += comb.get(val, 0)
        
    print(ret)


main()