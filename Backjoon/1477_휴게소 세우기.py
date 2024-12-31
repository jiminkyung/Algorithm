# 문제집 - 0x13강 - 이분탐색


# 문제: https://www.acmicpc.net/problem/1477
# 메모리: 32412KB / 시간: 40ms
from sys import stdin


input = stdin.readline

N, M, L = map(int, input().split())
# 0부터 고속도로의 마지막 부분 L까지의 구간을 계산
rest = [0] + sorted(map(int, input().split())) + [L]
gap = [rest[i+1] - rest[i] for i in range(N+1)]


def binary_search():
    start, end = 1, max(gap)

    while start <= end:
        mid = (start + end) // 2
        # 정확한 계산을 위해 (g-1) 후 연산.
        # ex) 구간이 500일경우 500//250 = 2가 되기 때문에 499//250 = 1이 되게끔 전처리
        cnt = sum((g-1) // mid for g in gap)

        if cnt <= M:  # 지을 수 있는 휴게소의 갯수가 M개 이하라면 길이를 늘려본다.
            end = mid - 1
        else:
            start = mid + 1

    return start


print(binary_search())