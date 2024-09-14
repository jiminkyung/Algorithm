# 최소 신장 트리


# 메모리: 85524KB / 시간: 1076ms
from sys import stdin


input = stdin.readline

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(a, b):
    fa, fb = find(a), find(b)

    if fa != fb:
        if rank[fa] < rank[fb]:
            parent[fa] = fb
        elif rank[fa] > rank[fb]:
            parent[fb] = fa
        else:
            parent[fb] = fa
            rank[fa] += 1
        return True
    return False

while True:
    m, n = map(int, input().split())

    if m == 0 and n == 0:
        break

    graph = [tuple(map(int, input().split())) for _ in range(n)]

    parent = list(range(m))
    rank = [0] * n

    graph.sort(key=lambda x: x[2])

    ret = total = 0
    for x, y, z in graph:
        total += z
        if union(x, y):
            ret += z
    
    print(total - ret)