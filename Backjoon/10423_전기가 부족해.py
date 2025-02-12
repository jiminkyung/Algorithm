# 문제집 - 0x1B강 - 최소 신장 트리


# 문제: https://www.acmicpc.net/problem/10423

# 1368_물대기 문제와 비슷함.
# 단, 이 문제에선 MST에 포함되지 않아도 되는 노드들이 정해져있음. (K 노드들)

# 1. 크루스칼 풀이
# 메모리: 49096KB / 시간: 228ms
from sys import stdin


input = stdin.readline

N, M, K = map(int, input().split())
installed = list(map(int, input().split()))
graph = [tuple(map(int, input().split())) for _ in range(M)]

# 발전소가 설치된 노드 -> 0번째 노드와 연결시켜주기
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


# 1. 일단 발전소가 설치되어 있는 노드들을 0번 노드와 연결시킴
for ins in installed:
    union(ins, 0)

# 2. 그래프 정렬 후 같은 집합이 아닐 경우에만 계산
graph.sort(key=lambda x: x[2])
ret = 0

for u, v, w in graph:
    if union(u, v):
        ret += w


print(ret)


# 2. 프림 풀이 (heapq)
# 메모리: 60680KB / 시간: 296ms
from sys import stdin
from heapq import heappop, heappush


input = stdin.readline
INF = float("inf")

N, M, K = map(int, input().split())

installed = set(map(int, input().split()))
graph = [[] for _ in range(N+1)]

for _ in range(M):
    u, v, w = map(int, input().split())

    graph[u].append((v, w))
    graph[v].append((u, w))

costs = [INF] * (N+1)
visited = [False] * (N+1)

heap = []
ret = cnt = 0

# 1. 본격적인 탐색을 시작하기 전, 발전소가 설치된 노드들을 힙에 넣어줌
for ins in installed:
    visited[ins] = True
    costs[ins] = 0
    for node, cost in graph[ins]:
        heappush(heap, (cost, node))

# 2. 힙이 존재하고 간선의 수(cnt)가 N-K개 이하일때까지만 진행
while heap and cnt < N - K:
    cost, node = heappop(heap)

    if visited[node]:
        continue

    visited[node] = True
    ret += cost
    cnt += 1

    for nxt, cost in graph[node]:
        if not visited[nxt] and cost < costs[nxt]:
            costs[nxt] = cost
            heappush(heap, (cost, nxt))


print(ret)