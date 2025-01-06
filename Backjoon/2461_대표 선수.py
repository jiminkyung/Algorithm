# 문제집 - 0x14강 - 투 포인터


# 문제: https://www.acmicpc.net/problem/2461

# 포인터만 사용하면 시간초과. heapq을 사용해야 통과할 수 있다.

# heap[0][0], heap[-1][0] 으로 최솟값, 최댓값을 구하려했으나 실패.
# 이유: heap은 형제 노드들 사이의 순서는 보장하지 않음.

# 메모리: 70676KB / 시간: 1448ms
from sys import stdin
from heapq import heappop, heappush


input = stdin.readline

N, M = map(int, input().split())
classes = [sorted(map(int, input().split())) for _ in range(N)]

heap = []
max_stat = 0

# 각 반의 최솟값을 heap에 추가
for i in range(N):
    heappush(heap, (classes[i][0], i, 0))
    max_stat = max(classes[i][0], max_stat)

min_diff = float("inf")

while True:
    # 현재 heap에서 최솟값을 꺼냄
    min_stat, class_idx, pos = heappop(heap)

    min_diff = min(max_stat - min_stat, min_diff)

    pos += 1  # 포인터를 1 증가시킴
    if pos == M:
        break

    # 해당 반의 다음 최솟값과 포인터를 삽입
    heappush(heap, (classes[class_idx][pos], class_idx, pos))
    max_stat = max(classes[class_idx][pos], max_stat)


print(min_diff)