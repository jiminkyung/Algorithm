# 문제집 - 0x1D강 - 다익스트라 알고리즘


# 문제: https://www.acmicpc.net/problem/5719

# 다익스트라 실행 -> 최단경로 삭제 -> 다익스트라 재실행
# 메모리: 36532KB / 시간: 180ms
from sys import stdin
from heapq import heappush, heappop


input = stdin.readline
INF = float("inf")


def first_dijkstra(N, S, graph: list) -> list:
    """ 첫번째 다익스트라로 최단경로들을 구함. 모든 경로는 prev에 저장. """
    prev = [[] for _ in range(N)]  # prev[x]: x의 이전 노드들
    dist = [INF] * N
    dist[S] = 0

    heap = [(0, S)]

    while heap:
        dis, curr = heappop(heap)

        if dist[curr] < dis:
            continue

        for nxt, d in graph[curr]:
            new_dis = dis + d
            if new_dis < dist[nxt]:  # 기존 경로값보다 작다면 갱신 후 prev[nxt]에 [새로운 경로] 할당
                prev[nxt] = [curr]
                dist[nxt] = new_dis
                heappush(heap, (new_dis, nxt))
            elif new_dis == dist[nxt]:  # 기존 경로값과 같다면 최단경로에 포함되므로 prev에 추가
                prev[nxt].append(curr)
    return prev


def remove(prev: list, graph: list, D):
    """ 기존의 graph에서 최단경로들을 삭제 """
    visited = set()
    stack = [D]

    while stack:
        curr = stack.pop()

        if curr in visited:  # 이미 삭제한 경로일경우 pass
            continue

        visited.add(curr)

        for prev_node in prev[curr]:
            # 기존 값을 토대로 갱신시켜줘야함.
            # => prev_node가 1, 2일경우 -> (1을 기준)graph 업데이트 -> (2 기준)앞에서 업데이트한 graph를 업데이트
            graph[prev_node] = [(v, w) for v, w in graph[prev_node] if v != curr]
            stack.append(prev_node)


def second_dijkstra(N, S, D, graph: list):
    """ 최단경로 삭제 후 두번째 다익스트라 실행 """
    dist = [INF] * N
    dist[S] = 0
    heap = [(0, S)]

    while heap:
        dis, curr = heappop(heap)

        if curr == D:
            return dis

        if dist[curr] < dis:
            continue

        for nxt, d in graph[curr]:
            new_dis = dis + d
            if new_dis < dist[nxt]:
                dist[nxt] = new_dis
                heappush(heap, (new_dis, nxt))
    return -1


def solve(N, M):
    graph = [[] for _ in range(N)]
    S, D = map(int, input().split())

    for _ in range(M):
        u, v, p = map(int, input().split())
        graph[u].append((v, p))

    prev = first_dijkstra(N, S, graph)
    remove(prev, graph, D)
    print(second_dijkstra(N, S, D, graph))


while True:
    N, M = map(int, input().split())

    if (N, M) == (0, 0):
        break

    solve(N, M)