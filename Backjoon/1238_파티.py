# 문제집 - 0x1D강 - 다익스트라 알고리즘


# 문제: https://www.acmicpc.net/problem/1238

# (마을 1,2,3...) -> X 까지 가는 시간을 구하려면 마을마다 다익스트라를 실행해야함.
# ⭐ 하지만 그래프를 뒤집으면 X -> (마을 1,2,3...): 마을에서 X까지 가는 시간이 됨.
# 즉, 기존의 X -> (마을 1,2,3...) 한번, 뒤집어서 한번 총 두번만 실행하면 된다!

# 메모리: 36532KB / 시간: 52ms
from sys import stdin
from heapq import heappop, heappush


input = stdin.readline
INF = int(1e9)

N, M, X = map(int, input().split())
X -= 1  # 0-based 처리했으므로 X도 -1 해줘야함.
graph = [[] for _ in range(N)]
reverse_graph = [[] for _ in range(N)]

for _ in range(M):
    u, v, w = map(int, input().split())
    graph[u-1].append((w, v-1))
    reverse_graph[v-1].append((w, u-1))

def dijkstra(start, g):
    heap = [(0, start)]
    time = [INF] * N
    time[start] = 0

    while heap:
        t, curr = heappop(heap)

        if time[curr] < t:
            continue

        for nxt_t, nxt in g[curr]:
            new_t = t + nxt_t
            if new_t < time[nxt]:
                time[nxt] = new_t
                heappush(heap, (new_t, nxt))
    return time

first = dijkstra(X, graph)
second = dijkstra(X, reverse_graph)

total_time = [sum(time) for time in zip(first, second)]
print(max(total_time))