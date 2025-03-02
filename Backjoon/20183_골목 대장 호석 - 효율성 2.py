# 문제집 - 0x1D강 - 다익스트라 알고리즘


# 문제: https://www.acmicpc.net/problem/20183

# 다시 풀어볼만한 문제 유형인듯.
# 메모리: 179380KB / 시간: 1752ms
from sys import stdin
from heapq import heappop, heappush


input = stdin.readline
INF = float("inf")

N, M, A, B, C = map(int, input().split())
graph = [[] for _ in range(N+1)]

for _ in range(M):
    u, v, w = map(int, input().split())
    graph[u].append((w, v))
    graph[v].append((w, u))


def dijkstra() -> int:
    costs = [INF] * (N+1)
    costs[A] = 0
    # (현재까지 가장 최대비용, 현재 위치, 총 비용) 형태로 힙에 저장
    # => 최소 힙이므로 자연스럽게 최소 "최대비용"을 꺼내게 됨.
    heap = [(0, A, 0)]

    while heap:
        max_cost, curr, total_cost = heappop(heap)

        if curr == B:
            return max_cost

        if costs[curr] < max_cost:
            continue

        for cost, nxt in graph[curr]:
            # 최대 비용, 총 비용 갱신
            new_max_cost = max(cost, max_cost)
            new_total_cost = total_cost + cost
            # 총 비용이 C 이하, 최대 비용이 기존 nxt의 최대 비용보다 작다면 업데이트
            if new_total_cost <= C and new_max_cost < costs[nxt]:
                costs[nxt] = new_max_cost
                heappush(heap, (new_max_cost, nxt, new_total_cost))
    
    return -1


print(dijkstra())