# 문제집 - 0x17강 - 우선순위 큐


# 문제: https://www.acmicpc.net/problem/1781

# 반례 1👉 https://www.acmicpc.net/board/view/152828
# 반례 2👉 https://www.acmicpc.net/board/view/123972
# 메모리: 64576KB / 시간: 608ms
from sys import stdin
from heapq import heappop, heappush


input = stdin.readline

N = int(input())
# 1. 데드라인 기준으로 오름차순 정렬
lst = [tuple(map(int, input().split())) for _ in range(N)]
lst.sort()

heap = []

# 2. 현재 시간(데드라인)보다 heap의 크기가 더 크다면 컵라면 수가 가장 적은 문제를 pop
# 데드라인 = 풀 수 있는 문제의 갯수
for deadline, noodle in lst:
    heappush(heap, noodle)

    if len(heap) > deadline:
        heappop(heap)

# 3. 최종적으로 남은 문제의 총 컵라면 갯수
print(sum(heap))