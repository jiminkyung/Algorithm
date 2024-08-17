# 최단 경로

# 역시 다익스트라 알고리즘을 사용해야 하는 문제.
# 1 -> v1 -> v2 -> V 와 1 -> v2 -> v1 -> V 의 값을 비교한다.


# 메모리: 64272KB / 시간: 572ms
from sys import stdin
from heapq import heappush, heappop


input = stdin.readline
N, E = map(int, input().split())
graph = [[] for _ in range(N+1)]

for _ in range(E):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

v1, v2 = map(int, input().split())

def dijkstra(start, end):
    distance = [float("inf")] * (N+1)
    distance[start] = 0
    queue = [(0, start)]

    while queue:
        curr_dis, curr_node = heappop(queue)

        if curr_dis > distance[curr_node]:
            continue

        for v, w in graph[curr_node]:
            new_dis = curr_dis + w
            if new_dis < distance[v]:
                distance[v] = new_dis
                heappush(queue, (new_dis, v))
    return distance[end]

ret1 = dijkstra(1, v1) + dijkstra(v1, v2) + dijkstra(v2, N)
ret2 = dijkstra(1, v2) + dijkstra(v2, v1) + dijkstra(v1, N)

ret = min(ret1, ret2)

print(ret if ret < float("inf") else -1)


# 함수를 일일이 실행하지 않고, 미리 실행한 뒤 참조하는 방법.
# 정확히 반만큼 절약됨!
# 메모리: 64264KB / 시간: 392ms
from sys import stdin
from heapq import heappush, heappop


input = stdin.readline
N, E = map(int, input().split())
graph = [[] for _ in range(N+1)]

for _ in range(E):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

v1, v2 = map(int, input().split())

def dijkstra(start):
    distance = [float("inf")] * (N+1)
    distance[start] = 0
    queue = [(0, start)]

    while queue:
        curr_dis, curr_node = heappop(queue)

        if curr_dis > distance[curr_node]:
            continue

        for v, w in graph[curr_node]:
            new_dis = curr_dis + w
            if new_dis < distance[v]:
                distance[v] = new_dis
                heappush(queue, (new_dis, v))
    return distance

from_one = dijkstra(1)
from_v1 = dijkstra(v1)
from_v2 = dijkstra(v2)

ret1 = from_one[v1] + from_v1[v2] + from_v2[N]
ret2 = from_one[v2] + from_v2[v1] + from_v1[N]
ret = min(ret1, ret2)

print(ret if ret < float("inf") else -1)