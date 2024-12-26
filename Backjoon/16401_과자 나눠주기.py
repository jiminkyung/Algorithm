# 문제집 - 0x13강 - 이분탐색


# 문제: https://www.acmicpc.net/problem/16401
# 메모리: 146176KB / 시간: 4768ms
from sys import stdin


input = stdin.readline

M, N = map(int, input().split())
snacks = sorted(map(int, input().split()))

start, end = 1, snacks[-1]
ret = 0

while start <= end:
    mid = (start + end) // 2

    # mid길이만큼 과자를 잘라 M개로 만들 수 있다면 성공
    cnt = sum(snack//mid for snack in snacks)

    if cnt >= M:
        ret = mid
        start = mid + 1
    else:
        end = mid - 1

print(ret)