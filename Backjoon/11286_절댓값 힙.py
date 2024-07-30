# 우선순위 큐

"""
입력값이 0일때,
- 절댓값이 가장 작은 값을 출력 후 배열에서 제거.
- 만약 절댓값이 가장 작은 값이 여러개라면 가장 작은 수를 출력 후 제거.
"""

# 메모리: 39824KB / 시간: 148ms
# 튜플형태로 push 가능.

from sys import stdin
from heapq import heappop, heappush


input()

heap = []

for x in stdin:
    x = int(x)

    if x:
        heappush(heap, (abs(x), x))
    else:
        print(heappop(heap)[1] if heap else 0)