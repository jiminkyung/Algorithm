# 구현
# 브루트포스 알고리즘
# 기하학


# 문제: https://www.acmicpc.net/problem/3097
# 메모리: 32412KB / 시간: 32ms
from sys import stdin


input = stdin.readline

def main():
    N = int(input())

    coords = [tuple(map(int, input().split())) for _ in range(N)]
    total_x = sum(coords[i][0] for i in range(N))
    total_y = sum(coords[i][1] for i in range(N))

    # 1. 경로 삭제 X
    print(total_x, total_y)

    min_diff = float("inf")

    # 2. 경로 삭제 O
    # 어차피 벡터값이고 +-만 들어있기 때문에 현재의 선택이 다음 선택에 영향 X, 1번 값에서 i번째 경로 값을 빼주기만 하면 됨.
    for i in range(N):
        x, y = coords[i]

        new_x = total_x - x
        new_y = total_y - y

        # i번째 경로를 제거했을때의 도착점 - 출발점 거리값
        diff = (new_x ** 2 + new_y ** 2) ** 0.5
        if diff < min_diff:
            min_diff = diff

    print(f"{min_diff:.2f}")


main()