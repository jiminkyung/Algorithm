# 수학
# 구현
# 브루트포스 알고리즘


# 문제: https://www.acmicpc.net/problem/1980
# 도움이 됐던 반례! 출처👉 https://www.acmicpc.net/board/view/104060
"""
1111 1717 9998

(1111 * 1) + (1717 * 5) + 302
-> 6 302
"""
# 메모리: 32412KB / 시간: 40ms
from sys import stdin


input = stdin.readline

def main():
    n, m, t = map(int, input().split())

    # 1. 콜라 마시는 시간 최소로
    # 2. 콜라 시간이 같다면 햄버거 최대로

    # 불벅, 타벅을 따로 구분하지 않아도 된다. 일단 더 효율적인 버거를 n으로 설정함.
    if n > m:
        n, m = m, n

    def check(n, m, t) -> int | int:
        min_coke = t
        max_burger = 0

        # 불벅을 최대한 많이 먹는 쪽으로 계산
        for i in range(t // m + 1):  # 타워버거
            rest_time = t - m * i
            for j in range(t // n + 1):  # 불고기버거
                # 남은 시간(콜라 마시는 시간)이 0이면 바로 반환
                if rest_time == 0:
                    return i + j, 0
                
                # 만약 남은 시간이 이전 콜라값보다 작거나 같다면,
                if 0 < rest_time <= min_coke:
                    # 같은 경우에는 버거를 최대한 많이 먹는경우로 선정
                    if rest_time == min_coke:
                        max_burger = max(max_burger, i + j)
                    # 작다면 현재 버거 갯수 저장
                    else:
                        max_burger = i + j

                    min_coke = rest_time
                
                # 매 턴마다 불벅타임만큼 감소시켜줌
                rest_time -= n
        return max_burger, min_coke


    max_burger, min_coke = check(n, m, t)
    print(max_burger, min_coke)


main()