# 최소 신장 트리(MST)


# 문제: https://www.acmicpc.net/problem/1922

# 1. 크루스칼 알고리즘을 사용한 풀이.
# rank를 생성하지 않아도 실행시간은 같다. 메모리는 더 효율적이다.
# 메모리: 46780KB / 시간: 232ms
from sys import stdin


input = stdin.readline

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(a, b):
    if a != b:
        if a < b:
            parent[b] = a
        else:
            parent[a] = b

N = int(input())
M = int(input())

edge = [tuple(map(int, input().split())) for _ in range(M)]
edge.sort(key=lambda x: x[2])  # 비용(가중치)를 기준으로 정렬

parent = list(range(N+1))

total_cost = 0
for u, v, w in edge:
    u, v = find(u), find(v)

    if u != v:
        union(u, v)
        total_cost += w

print(total_cost)


# rank 사용
# 메모리: 47804KB / 시간: 232ms
from sys import stdin


input = stdin.readline

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(a, b):
    if a != b:
        if rank[a] < rank[b]:
            parent[a] = b
        elif rank[a] > rank[b]:
            parent[b] = a
        else:
            parent[b] = a
            rank[a] += 1

N = int(input())
M = int(input())

edge = [tuple(map(int, input().split())) for _ in range(M)]
edge.sort(key=lambda x: x[2])

parent = list(range(N+1))
rank = [0] * (N+1)

total_cost = 0
for u, v, w in edge:
    u, v = find(u), find(v)

    if u != v:
        union(u, v)
        total_cost += w

print(total_cost)


# 2. 프림 알고리즘도 사용해보자.
# 메모리: 62144KB / 시간: 404ms
from sys import stdin
from heapq import heappush, heappop


input = stdin.readline

def prim():
    heap = [(0, 1)]
    visited = [False] * (N+1)
    total_cost = 0

    while heap:
        cost, node = heappop(heap)
        if not visited[node]:  # 힙에서 꺼낸 다음 방문처리
            visited[node] = True
            total_cost += cost

            for nxt_node, nxt_cost in edge[node]:
                if not visited[nxt_node]:
                    heappush(heap, (nxt_cost, nxt_node))
    
    return total_cost

N, M = int(input()), int(input())
edge = [[] for _ in range(N+1)]

for _ in range(M):
    u, v, w = map(int, input().split())
    edge[u].append((v, w))
    edge[v].append((u, w))

print(prim())