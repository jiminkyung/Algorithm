# 문제집 - 0x1B강 - 최소 신장 트리


# 문제: https://www.acmicpc.net/problem/1774

# 블로그에 업로드하기 전 다시 풀어봤다.
# 🚨 다시 풀면서도 실수했던 부분
    # 이미 연결된 행성들로 주어진 M개의 행성 쌍들은 "MST"라는 보장이 없음!
    # 즉, (a, b), (c, d)로 주어졌을때, a-b / c-d 별개로 봐야함. 전체가 이어진건 아니다.

# 1. 다시 풀어본 풀이 (프림)
# 메모리: 33432KB / 시간: 276ms
from sys import stdin


input = stdin.readline
INF = float("inf")

def main():
    N, M = map(int, input().split())

    # 1. 행성 좌표와 이미 연결된 행성들의 정보를 저장
    graph = [tuple(map(int, input().split())) for _ in range(N)]
    linked = [set() for _ in range(N)]  # linked[a] = a와 연결된 행성들

    for _ in range(M):
        a, b = map(lambda x: int(x)-1, input().split())
        linked[a].add(b)
        linked[b].add(a)
    
    # 2. 프림 알고리즘 진행
    visited = [False] * N
    costs = [INF] * N
    costs[0] = 0
    ret = 0.0
    
    for _ in range(N):
        min_node = -1
        min_cost = INF

        for i in range(N):
            if not visited[i] and costs[i] < min_cost:
                min_node = i
                min_cost = costs[i]
        
        visited[min_node] = True
        ret += min_cost ** 0.5

        # 2-1. 현재 행성에서 다른 행성까지의 거리 계산
        # 이미 방문한 행성이라면 넘어감.

        # 현재 행성과 연결되어있는 행성이라면, 거리값을 0으로 업데이트함.
        # 아니라면, 거리계산 후 기존 거리값보다 작을 경우에만 거리값 업데이트.
        for nxt, (x, y) in enumerate(graph):
            if visited[nxt]:
                continue

            if nxt in linked[min_node]:
                costs[nxt] = 0
            else:
                cost = (graph[min_node][0] - x) ** 2 + (graph[min_node][1] - y) ** 2
                if cost < costs[nxt]:
                    costs[nxt] = cost
    
    # 3. 두번째 자리에서 반올림한 결과 출력
    print(f"{ret:.2f}")  # f-string을 사용하면 자동으로 반올림 가능


main()


# 힙을 사용하면 아주 조금 더 빨라짐.
# 메모리: 36532KB / 시간: 240ms
from sys import stdin
from heapq import heappush, heappop


input = stdin.readline
INF = float("inf")

def main():
    N, M = map(int, input().split())

    # 1. 행성 좌표와 이미 연결된 행성들의 정보를 저장
    graph = [tuple(map(int, input().split())) for _ in range(N)]
    linked = [set() for _ in range(N)]  # linked[a] = a와 연결된 행성들

    for _ in range(M):
        a, b = map(lambda x: int(x)-1, input().split())
        linked[a].add(b)
        linked[b].add(a)
    
    # 2. 프림 알고리즘 진행
    heap = [(0, 0)]
    cnt = 0
    
    visited = [False] * N
    costs = [INF] * N
    costs[0] = 0
    ret = 0.0
    
    while heap:
        cost, curr = heappop(heap)
        
        if visited[curr]:
            continue
        
        visited[curr] = True
        ret += cost ** 0.5
        cnt += 1
        
        if cnt >= N:
            break
        
        # 2-1. 현재 행성에서 다른 행성까지의 거리 계산
        # 이미 방문한 행성이라면 넘어감.

        # 현재 행성과 연결되어있는 행성이라면, 거리값을 0으로 업데이트함.
        # 아니라면, 거리계산 후 기존 거리값보다 작을 경우에만 거리값 업데이트.
        for nxt, (x, y) in enumerate(graph):
            if visited[nxt]:
                continue
            
            if nxt in linked[curr]:
                costs[nxt] = 0
                heappush(heap, (0, nxt))
            else:
                nxt_cost = (graph[curr][0] - x) ** 2 + (graph[curr][1] - y) ** 2
                if nxt_cost < costs[nxt]:
                    costs[nxt] = nxt_cost
                    heappush(heap, (nxt_cost, nxt))
    
    # 3. 두번째 자리에서 반올림한 결과 출력
    print(f"{ret:.2f}")  # f-string을 사용하면 자동으로 반올림 가능


main()


# 2. 기존에 통과했던 풀이 (크루스칼)
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


# 아래는 다른분이 작성한 풀이
# 출처👉 https://www.acmicpc.net/source/52778455
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