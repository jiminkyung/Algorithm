# 자료구조
# 해시와 맵


# 문제: https://www.acmicpc.net/problem/2358

# 문제 설명이 좀 헷갈린다. 주의!!
# 여기서 말하는 "직선"은 점끼리 연결했을때의 직선이 아님.
# 임의의 직선이 점들을 꿰뚫고 지나간다고 생각하면 됨.
# + 같은 좌표가 2개 주어져도 다른 점으로 취급하니 "두 점" 조건을 충족함.

# 따라서 (0, 1), (0, 2), (0, 3), (0, 3)에서 x=0인 y축 평행 직선은 한개.
# 여기서 (0, 3), (0, 3)의 경우 y=3이므로 x축에 평행하니까 또 한개. 답은 두개다.

# 관련 질문글👉 https://www.acmicpc.net/board/view/83686

# 메모리: 52916KB / 시간: 152ms
from sys import stdin


input = stdin.readline

def main():
    n = int(input())
    # x, y = list(zip(*[tuple(map(int, input().split())) for _ in range(n)]))
    coord = [tuple(map(int, input().split())) for _ in range(n)]

    X = {}  # x가 같은 좌표들 (y축에 평행)
    Y = {}  # y가 같은 좌표들 (x축에 평행)

    for x, y in coord:
        X[x] = X.get(x, 0) + 1
        Y[y] = Y.get(y, 0) + 1
    
    ret = 0

    for _, val in X.items():
        # 같은 좌표가 2개 이상일경우에만 카운트
        if val >= 2:
            ret += 1
    
    for _, val in Y.items():
        if val >= 2:
            ret += 1
    
    print(ret)


main()