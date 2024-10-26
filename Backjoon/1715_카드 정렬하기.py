# 문제집 - BOJ 길라잡이 베타 (1)


# 문제: https://www.acmicpc.net/problem/1715
# 참고하면 좋은 글👉 https://www.acmicpc.net/board/view/140700

# 메모리: 33972KB / 시간: 176ms
from sys import stdin
from heapq import heappop, heappush


input = stdin.readline

N = int(input())
heap = []

for _ in range(N):
    heappush(heap, int(input()))

ret = 0
while len(heap) > 1:
    # 힙에서 가장 작은 값 두개를 빼 ret에 더해준 뒤 다시 힙에 추가한다.
    # [10, 20, 50] => [30, 50] => [80] 이므로 자연스럽게 누적합 처리.
    curr = heappop(heap) + heappop(heap)
    ret += curr

    heappush(heap, curr)

print(ret)