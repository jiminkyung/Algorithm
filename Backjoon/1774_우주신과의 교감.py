# 최소 신장 트리


# 기존의 통로 길이값은 제외한다.
# 메모리: 101264KB / 시간: 976ms
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

N, M = map(int, input().split())

coordinate = {i: tuple(map(float, input().split())) for i in range(1, N+1)}
edges = []

parent = list(range(N+1))
rank = [0] * (N+1)

# tmp = {}

for i in range(1, N+1):
    for j in range(1, i):
        (x1, y1), (x2, y2) = coordinate[i], coordinate[j]
        distance = (abs(x1-x2)**2 + abs(y1-y2)**2)**0.5
        edges.append((i, j, distance))
        # tmp[(i, j)] = distance

for _ in range(M):
    a, b = map(int, input().split())
    # ret += tmp.get((a, b), tmp[(b, a)])
    union(find(a), find(b))

edges.sort(key=lambda x: x[2])

ret = 0.0
for a, b, dis in edges:
    a, b = find(a), find(b)

    if a != b:
        union(a, b)
        ret += dis

print(f"{ret:.2f}")


# 실행시간 372ms, 메모리 31256KB인 코드.
# 크루스칼 알고리즘이 아닌 프림 알고리즘을 사용했다.
import sys

def get_ints():
    return tuple(int(x) for x in sys.stdin.readline().strip().split())

def dist(G, points, i, j) -> int:
    if i == j:
        return 0
    if j in G[i]:
        return 0
    return (points[i][0] - points[j][0]) ** 2 + (points[i][1] - points[j][1]) ** 2

def argmin(a: list, exc: set):
    res, val, first = None, None, True
    for i, x in enumerate(a):
        if i not in exc:
            if first:
                res, val, first = i, x, False
            elif x < val:
                res = i
                val = x
    return res, val

def main():
    n, m = get_ints()

    points = []
    for _ in range(n):
        points.append(get_ints())
    
    G = [set() for _ in range(n)]
    for _ in range(m):
        x, y = get_ints()
        G[x - 1].add(y - 1)
        G[y - 1].add(x - 1)

    visited = {0}
    ds = [dist(G, points, 0, i) for i in range(n)]

    res = 0.0

    while len(visited) < n:
        p, d = argmin(ds, visited)
        visited.add(p)
        res += d ** .5
        for cand in range(n):
            if cand not in visited:
                ds[cand] = min(ds[cand], dist(G, points, cand, p))

    print("{:.2f}".format(round(res, 2)))

main()