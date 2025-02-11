# 문제집 - 0x1B강 - 최소 신장 트리


# 문제: https://www.acmicpc.net/problem/1368

# 크루스칼 알고리즘으로 풀이할경우, 가상의 논 N을 설정해야함.
# 우물을 직접 파는 경우 => 가상의 논 N과 연결하는경우

# 1. 크루스칼 알고리즘 풀이
# 메모리: 38240KB / 시간: 88ms
from sys import stdin


input = stdin.readline

N = int(input())
water = [int(input()) for _ in range(N)]

# 가상의 논 N을 설정해야할듯.
# (i, N) => i번째 논에서 직접 우물을 파는 경우
graph = [(i, N, water[i]) for i in range(N)]

for i in range(N):
    line = list(map(int, input().split()))
    for j in range(i):
        graph.append((i, j, line[j]))

parent = list(range(N+1))

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]


def union(a, b):
    a, b = find(a), find(b)

    if a != b:
        if a < b:
            parent[b] = a
        else:
            parent[a] = b
        return True
    return False


ret = 0
graph.sort(key=lambda x: x[2])

for u, v, w in graph:
    if union(u, v):
        ret += w


print(ret)


# 2. 프림 알고리즘 풀이 (리스트)
# 메모리: 35480KB / 시간: 72ms
from sys import stdin


input = stdin.readline

N = int(input())
water = [int(input()) for _ in range(N)]
graph = [tuple(map(int, input().split())) for _ in range(N)]
cost = [float("inf")] * N
visited = [False] * N

# 시작점 찾기 (가장 작은 우물 비용)
start = -1
start_water = float("inf")

for i in range(N):
    if water[i] < start_water:
        start = i
        start_water = water[i]

cost[start] = start_water
ret = 0

for _ in range(N):
    min_cost = float("inf")
    min_node = -1

    for i in range(N):
        if not visited[i] and cost[i] < min_cost:
            min_cost = cost[i]
            min_node = i
    
    visited[min_node] = True
    ret += min_cost

    for nxt in range(N):
        if visited[nxt]:
            continue
        # 각각의 비용을 독립적으로 비교
        cost[nxt] = min(cost[nxt], graph[min_node][nxt], water[nxt])

print(ret)


# 3. 프림 알고리즘 풀이 (heapq)
# 메모리: 37556KB / 시간: 72ms
from sys import stdin
from heapq import heappush, heappop


input = stdin.readline

N = int(input())
water = [int(input()) for _ in range(N)]
graph = [tuple(map(int, input().split())) for _ in range(N)]

costs = [float("inf")] * N
visited = [False] * N

# 시작점 찾기 (가장 작은 우물 비용)
start = -1
start_water = float("inf")

for i in range(N):
    if water[i] < start_water:
        start = i
        start_water = water[i]

heap = [(start_water, start)]

costs[start] = start_water
ret = cnt = 0

while heap:
    cost, node = heappop(heap)

    if visited[node]:
        continue

    visited[node] = True
    ret += cost
    cnt += 1

    if cnt >= N:
        break

    for nxt, cost in enumerate(graph[node]):
        if visited[nxt]:
            continue

        # 다른 논과 연결하는 비용, 우물을 파는 비용 중 더 작은 값을 선택
        new_cost = min(cost, water[nxt])

        # 해당 값이 최소비용보다 작다면 업데이트 후 힙에 추가한다.
        if new_cost < costs[nxt]:
            heappush(heap, (new_cost, nxt))
            costs[nxt] = new_cost


print(ret)