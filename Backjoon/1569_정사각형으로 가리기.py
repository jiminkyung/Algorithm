# 구현
# 기하학


# 문제: https://www.acmicpc.net/problem/1569

"""
정사각형의 꼭짓점이 될 수 있는 후보군은 두 가지다.
1. 좌측 하단 (min_x, min_y)
2. 우측 상단 (max_x, max_y)

각 후보를 기준으로 +길이 만큼의 둘레 안에 모든 좌표가 들어간다면 성공.
1. 좌측 하단의 경우
- min_x ~ min_x+길이 안에 x 좌표가 들어간다면
    - y좌표가 min_y or min_y+길이 여야함.
- min_y ~ min_y+길이 안에 y 좌표가 들어간다면
    - x좌표가 min_x or min_x+길이 여야함.
2. 우측 상단의 경우
- max_x-길이 ~ max_x 안에 x 좌표가 들어간다면
    - y좌표가 max_y-길이 or max_y 여야함.
- max_y-길이 ~ max_y 안에 y 좌표가 들어간다면
    - x좌표가 max_x-길이 or max_x 여야함.

참고👉 https://velog.io/@financeloper/%EB%B0%B1%EC%A4%80-1569-%EC%A0%95%EC%82%AC%EA%B0%81%ED%98%95%EC%9C%BC%EB%A1%9C-%EA%B0%80%EB%A6%AC%EA%B8%B0
"""

# 메모리: 32412KB / 시간: 40ms
from sys import stdin


input = stdin.readline

def main():
    N = int(input())
    coord = [tuple(map(int, input().split())) for _ in range(N)]
    coord_x = [coord[i][0] for i in range(N)]
    coord_y = [coord[i][1] for i in range(N)]

    max_x, min_x = max(coord_x), min(coord_x)
    max_y, min_y = max(coord_y), min(coord_y)

    size = max(max_x - min_x, max_y - min_y)

    def check(x, y, size):
        for nx, ny in coord:
            if x <= nx <= x + size and ny in (y, y + size):
                continue
            if y <= ny <= y + size and nx in (x, x + size):
                continue
            break
        else:
            return True
        return False

    if check(min_x, min_y, size) or check(max_x - size, max_y - size, size):
        print(size)
    else:
        print(-1)


main()


# 테스트 코드. 이건 그냥 좌표를 시각적으로 보기 위해 만들어봄.
def test():
    N = int(input())
    coord = [["□"] * 21 for _ in range(21)]

    for _ in range(N):
        x, y = map(int, input().split())
        coord[10 - y][10 + x] = "■"

    coord[10][10] = "▣"
    for line in coord:
        print(*line)