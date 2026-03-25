# 수학
# 미적분학


# 문제: https://www.acmicpc.net/problem/3753
# 메모리: 32412KB / 시간: 32ms
from sys import stdin


def main():
    # 각 N개의 이익은 T(C - TN)임.
    # = -NT^2 + CT

    # 이차함수 ax^2 + bx 의 꼭짓점 x는 -b / 2a 이므로,
    # 꼭짓점 x(=T)는 -C / -2N = C / 2N 임.
    # => 이 값이 최고지점의 T 값이다.
    data = stdin.read().splitlines()

    for d in data:
        N, C = map(int, d.split())

        if N == 0:
            print(0)
            continue

        # 딱 떨어지지 않는다면(ex: 4.5) 둘 중 결과값이 더 큰 값으로 선택. 같다면 더 작은 T값으로.
        T = int(C / (2 * N))
        ret_1 = T * (C - T*N)
        ret_2 = (T+1) * (C - (T+1)*N)

        if ret_1 < ret_2:
            print(T + 1)
        else:
            # T는 0 이상이어야 하므로 최소 0에 맞춰줌.
            print(max(T, 0))


main()