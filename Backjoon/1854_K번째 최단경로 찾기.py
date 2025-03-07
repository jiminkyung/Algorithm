# 문제집 - 0x1D강 - 다익스트라 알고리즘


# 문제: https://www.acmicpc.net/problem/1854

# 21944_문제추천시스템 ver2 가 생각나는 문제... 2차원 힙으로 구성해야함.
# 다시 풀어볼만한 문제 유형

# 메모리: 66188KB / 시간: 2148ms
from sys import stdin
from heapq import heappush, heappop


input = stdin.readline
INF = float("inf")

N, M, K = map(int, input().split())
graph = [[] for _ in range(N+1)]

for _ in range(M):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))  # 🚨 단방향으로 저장해야함


def dijkstra():
    # 🗝️ dist[x]: 출발지부터 x까지의 최소 비용들을 저장. 최대 힙.
    dist = [[] for _ in range(N+1)]
    heappush(dist[1], 0)
    heap = [(0, 1)]

    while heap:
        cost, curr = heappop(heap)

        for nxt, c in graph[curr]:
            new_cost = cost + c

            # 1. dist[nxt]의 힙 길이가 K 미만일경우
            if len(dist[nxt]) < K:
                # dist[nxt]의 힙, 최단거리값을 비교할 힙 두곳에 모두 삽입
                heappush(dist[nxt], -new_cost)
                heappush(heap, (new_cost, nxt))
            # 2. dist[nxt]에서 가장 큰 값보다 새로운 비용이 작을경우
            elif new_cost < -dist[nxt][0]:
                # 가장 큰 비용을 빼낸 후 새로운 비용 삽입
                heappop(dist[nxt])
                heappush(dist[nxt], -new_cost)
                heappush(heap, (new_cost, nxt))  # 비교 힙에도 삽입
    return dist


dist = dijkstra()

for i in range(1, N+1):
    # dist[i]의 힙 길이가 K 미만이면 -1, 아니면 가장 작은 값(힙에 들어있는 값 중에서 가장 큰 값)을 출력
    ret = -dist[i][0] if len(dist[i]) == K else -1
    print(ret)