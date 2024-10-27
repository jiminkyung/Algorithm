# 문제집 - BOJ 길라잡이 베타 (1)


# 문제: https://www.acmicpc.net/problem/1655
# 메모리: 37132KB / 시간: 224ms
from sys import stdin
from heapq import heappop, heappush


input = stdin.readline

N = int(input())
left, right = [], []  # left: 최대힙(중간값보다 작거나 같은), right: 최소힙(중간값보다 큰)

for _ in range(N):
    num = int(input())
    
    if len(left) == len(right):
        heappush(left, -num)
    else:
        heappush(right, num)

    if right and -left[0] > right[0]:
        l, r = heappop(left), heappop(right)
        heappush(right, -l)
        heappush(left, -r)

    print(-left[0])