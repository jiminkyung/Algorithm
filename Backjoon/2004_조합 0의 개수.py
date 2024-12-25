# 문제집 - 0x12강 - 수학


# 문제: https://www.acmicpc.net/problem/2004

# 참고했던 글👉 https://www.acmicpc.net/board/view/66047
# 5의 갯수끼리만, 2의 갯수끼리만 각각 구한 뒤 더 작은 값을 선택해야한다.
# 1676_팩토리얼 0의 개수와 비슷한 문제이지만 "조합"문제이므로 2의 개수도 고려해야한다.
# 조합계산을 진행하면서 2와 5의 갯수는 서로 다른 비율로 줄어들게 되므로, 각각 독립적으로 계산 후 마지막에 비교해야함.

# 메모리: 32544KB / 시간: 40ms
from sys import stdin


input = stdin.readline

N, M = map(int, input().split())


def counting(k, num):
    cnt = 0
    m = num

    while m <= k:
        cnt += k // m
        m *= num
    return cnt


ret1 = counting(N, 5) - (counting(M, 5) + counting(N-M, 5))
ret2 = counting(N, 2) - (counting(M, 2) + counting(N-M, 2))

print(min(ret1, ret2))