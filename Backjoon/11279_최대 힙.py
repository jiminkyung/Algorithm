# 우선순위 큐

"""
파이썬은 기본적으로 최소힙.
최대힙으로 사용하려면 음수값으로(-) 넣어주면 된다.

입력값 x가 0이라면 heap에서 가장 큰 값을 출력 후 제거.
만약 heap이 비어있는 상태라면 그냥 0 출력.
"""

# 메모리: 37044KB / 시간: 116ms

from sys import stdin
import heapq


input = stdin.readline

N = int(input())
heap = []

for _ in range(N):
    x = int(input())

    if x:
        heapq.heappush(heap, -x)
    else:
        print(-heapq.heappop(heap) if heap else 0)