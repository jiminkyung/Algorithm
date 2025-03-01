# 문제집 - 0x1D강 - 다익스트라 알고리즘


# 문제: https://www.acmicpc.net/problem/17835

# U -> V 형식의 그래프를 V -> U 형식으로 저장.
# ⭐ 그리고 V를 모두 힙에 넣어둔 뒤 다익스트라를 실행해야함!
# 즉, 다익스트라를 동시에 실행하는것임.
# 이게 가능한 이유는 아마... 특정 K를 기준으로 답을 구하는게 아닌, 전체 값 중 가장 최대값만 찾으면 되기 때문인듯?

# 메모리: 123272KB / 시간: 1388ms
from sys import stdin
from heapq import heappush, heappop


input = stdin.readline
INF = float("inf")  # 🚨 int(1e9)로 설정해두면 83%에서 틀림

N, M, K = map(int, input().split())
# 그래프를 뒤집어서 저장해두는게 좋을듯?
graph = [[] for _ in range(N)]

for _ in range(M):
    U, V, C = map(int, input().split())
    graph[V-1].append((C, U-1))

# 0-based 처리
places = list(map(lambda x: int(x)-1, input().split()))

def dijkstra() -> list:
    dist = [INF] * N
    heap = []

    # 모든 면접장들을 힙에 넣고 한꺼번에 돌림
    for place in places:
        heappush(heap, (0, place))
        dist[place] = 0

    while heap:
        c, curr = heappop(heap)

        if dist[curr] < c:
            continue

        for cost, nxt in graph[curr]:
            new_cost = c + cost
            if new_cost < dist[nxt]:
                dist[nxt] = new_cost
                heappush(heap, (new_cost, nxt))
    
    # dist[x]: x와 가장 가까운 면접장과 x의 거리
    return dist


dist = dijkstra()
max_dist = max(dist)

print(dist.index(max_dist) + 1, max_dist, sep="\n")