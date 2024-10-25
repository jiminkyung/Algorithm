# 문제집 - BOJ 길라잡이 베타 (1)


# 문제: https://www.acmicpc.net/problem/2512
# 메모리: 32140KB / 시간: 76ms
from sys import stdin


input = stdin.readline

N = int(input())
budget = list(map(int, input().split()))
target = int(input())

start, end = 0, max(budget)

if sum(budget) <= target:
    print(end)
else:
    ret = 0

    while start <= end:
        mid = (start + end) // 2

        total = 0
        for bud in budget:  # mid와 기존값 중 더 작은값을 total에 추가
            total += min(bud, mid)
        
        if total <= target:
            ret = mid
            start = mid + 1
        else:
            end = mid - 1

    print(ret)