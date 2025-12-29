# 수학
# 기하학


# 문제: https://www.acmicpc.net/problem/3063
# 메모리: 32412KB / 시간: 40ms
from sys import stdin


input = stdin.readline

def main():
    T = int(input())

    for _ in range(T):
        print(solve())


def solve():
    # 좌측하단 꼭짓점, 우측상단 꼭짓점
    x1, y1, x2, y2, x3, y3, x4, y4 = map(int, input().split())

    # 첫번째 직사각형의 원래 넓이
    full = (x2 - x1) * (y2 - y1)

    # 겹치는 부분의 가로, 세로 길이
    # 가로의 경우, 겹치는 부분의 시작점: 두 시작점 중 더 오른쪽에 위치한 값. 끝점: 두 끝점 중 더 왼쪽에 위치한 값.
    # 세로의 경우, 겹치는 부분의 시작점: 두 시작점 중 더 위쪽에 위치한 값. 끝점: 두 끝점 중 더 아래쪽에 위치한 값.
    over_x = min(x2, x4) - max(x1, x3)
    over_y = min(y2, y4) - max(y1, y3)

    # 겹치는 부분이 없다면 원래 넓이 반환
    if over_x <= 0 or over_y <= 0:
        return full
    
    return full - (over_x * over_y)


main()