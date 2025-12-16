# 수학
# 기하학
# 조합론
# 집합과 맵


# 문제: https://www.acmicpc.net/problem/3000
# 메모리: 49844KB / 시간: 152ms
from sys import stdin


input = stdin.readline

def main():
    N = int(input())
    coord = [tuple(map(int, input().split())) for _ in range(N)]
    X = {}
    Y = {}

    # 🚨 중복 좌표는 주어지지 않음.
    # X[i]: x좌표가 i인 지점의 갯수
    # Y[j]: y좌표가 j인 지점의 갯수
    for x, y in coord:
        X[x] = X.get(x, 0) + 1
        Y[y] = Y.get(y, 0) + 1
    
    cnt = 0
    for x, y in coord:
        # x좌표가 동일한 점의 갯수 * y좌표가 동일한 점의 갯수
        # (자기 자신은 제외해야하므로 -1 처리)
        cnt += (X[x] - 1) * (Y[y] - 1)
    
    print(cnt)


main()