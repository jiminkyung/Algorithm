# 문제집 - 0x17강 - 우선순위 큐


# 문제: https://www.acmicpc.net/problem/13975

# 최종 파일 크기는 순서가 어떻든 똑같다.
# 하지만 비용이 최소가 되려면 크기가 작은 파일끼리 더해나가야 함.

# 메모리: 138080KB / 시간: 7644ms
from sys import stdin
from heapq import heappush, heappop


input = stdin.readline

T = int(input())
for _ in range(T):
    K = int(input())
    files = []

    for file in map(int, input().split()):
        heappush(files, file)

    total_cost = 0

    while len(files) > 1:
        x1, x2 = heappop(files), heappop(files)
        total_cost += x1 + x2
        heappush(files, x1 + x2)

    print(total_cost)