# 문제집 - 0x1D강 - 다익스트라 알고리즘


# 문제: https://www.acmicpc.net/problem/1916
# 메모리: 58232KB / 시간: 272ms
from sys import stdin
from heapq import heappush, heappop


input = stdin.readline

N = int(input())
M = int(input())

graph = [[] for _ in range(N+1)]

for _ in range(M):
    a, b, cost = map(int, input().split())
    graph[a-1].append((cost, b-1))  # 0-based 처리


def dijkstra(start, end) -> int:
    costs = [int(1e9)] * N
    costs[start] = 0
    heap = [(0, start)]

    while heap:
        cost, curr = heappop(heap)

        if costs[curr] < cost:  # 기존 비용이 더 작다면 넘어감
            continue

        for nxt_cost, nxt in graph[curr]:
            new_cost = cost + nxt_cost
            if new_cost < costs[nxt]:
                costs[nxt] = new_cost
                heappush(heap, (new_cost, nxt))
    return costs[end]


start, end = map(int, input().split())
print(dijkstra(start-1, end-1))