# 문제집 - 0x17강 - 우선순위 큐


# 문제: https://www.acmicpc.net/problem/2075
# 메모리: 35508KB / 시간: 1612ms
from sys import stdin
from heapq import heappop, heappush


input = stdin.readline

N = int(input())
heap = []

for _ in range(N):
    for num in map(int, input().split()):
        heappush(heap, num)
        # 힙의 길이가 N을 넘어가면 제일 작은값을 빼줌
        if len(heap) > N:
            heappop(heap)

print(heap[0])