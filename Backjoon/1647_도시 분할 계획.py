# 문제집 - 0x1B강 - 최소 신장 트리


# 문제: https://www.acmicpc.net/workbook/view/9907

# 크루스칼 알고리즘 사용
# 메모리: 212620KB / 시간: 2384ms
from sys import stdin


input = stdin.readline

N, M = map(int, input().split())
graph = [tuple(map(int, input().split())) for _ in range(M)]
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


graph.sort(key=lambda x: x[2])
max_cost = 0

ret = 0

# 1. 최소 신장 트리를 만들며 가장 비용이 큰 간선을 저장해둔다.
for u, v, w in graph:
    if union(u, v):
        max_cost = max(w, max_cost)
        ret += w

# 2. 완성된 최소 신장 트리에서 저장해뒀던 간선만 제거
ret -= max_cost

print(ret)