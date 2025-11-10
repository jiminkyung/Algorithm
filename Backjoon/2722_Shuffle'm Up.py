# 구현
# 자료 구조
# 문자열
# 브루트포스 알고리즘
# 시뮬레이션


# 문제: https://www.acmicpc.net/problem/2722
# 메모리: 32412KB / 시간: 32ms
from sys import stdin


input = stdin.readline

def main():
    def solve() -> int:
        C = int(input())  # 칩의 갯수

        s1 = list(input().rstrip())
        s2 = list(input().rstrip())
        target = list(input().rstrip())  # 목표 형태

        # 초기값. 만약 이 값이 또 나온다면 target으로 만들 수 없음을 의미함.
        # [s2[0], s1[0], s2[1], s1[1]...]
        start = [x for pair in zip(s2, s1) for x in pair]
        turn = 0

        while True:
            s12 = [x for pair in zip(s2, s1) for x in pair]

            # 초기값이 또 나온다면 -1 반환
            if turn and s12 == start:
                return -1
            # 목표 형태와 일치한다면 턴 수 반환
            if s12 == target:
                return turn + 1

            s1 = s12[:C]
            s2 = s12[C:]
            turn += 1


    T = int(input())

    for _ in range(T):
        print(solve())


main()