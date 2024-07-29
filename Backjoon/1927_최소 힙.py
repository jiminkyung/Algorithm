# 우선순위 큐

# 11279_최대 힙.py 와 같음.
# 메모리: 37044KB / 시간: 116ms

from sys import stdin
import heapq


input()

heap = []

for x in stdin:
    x = int(x)

    if x:
        heapq.heappush(heap, x)
    else:
        print(heapq.heappop(heap) if heap else 0)