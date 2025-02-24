# 문제집 - 0x1C강 - 플로이드 알고리즘


# 문제: https://www.acmicpc.net/problem/23258

# PyPy3로도 실패하다가 결국 다른 풀이를 참고해서 통과했다... 다시 풀어볼만한 문제다.
# 참고👉 https://thought-process-ing.tistory.com/388

# 기본적인 로직은 다음과 같다.
# 먹을 수 있는 정수의 한도가 C일경우, C-1번 노드까지만 방문이 가능하다.
# 정수의 양 = 2 ^ 노드번호 이므로, C보다 큰 노드를 방문하게되면 한도초과가 되기 때문이다.
# 따라서 리스트를 3차원으로 생성 후, 플로이드 워셜을 통해 C-1 이하의 노드만 경유한 최단경로값을 찾아낸다.

# 메모리: 332088KB / 시간: 1460ms
from sys import stdin


input = stdin.readline
INF = int(1e9)

N, Q = map(int, input().split())
graph = [[[INF] * (N+1) for _ in range(N+1)] for _ in range(N+1)]

# graph[C][i][j] = C번 노드까지를 경유지로 삼았을때 i-j 최단거리
# 초기화시에는 아무런 노드도 경유하지 않기 때문에 graph[0][i][j]에 값을 저장한다.
for i in range(1, N+1):
    graph[0][i][i] = 0
    for j, dist in enumerate(map(int, input().split()), start=1):
        if i != j and dist != 0:
            graph[0][i][j] = dist

for k in range(1, N+1):
    for i in range(1, N+1):
        for j in range(1, N+1):
            #🗝️ k번 노드를 경유지로 추가할지 말지 결정하는것과 같음!!
            # 1️⃣ k-1번까지를 경유지로 삼았을때의 i-j값
            # 2️⃣ k-1번까지를 경유지로 삼았을때의 i-k + k-j값
            # 둘 중 더 작은값을 "k번까지를 경유지로 삼았을때의 i-j 최단거리"값으로 설정함.
            # 기존의 graph[k][i][j]값과 비교하지 않는 이유는, 일반적인 플로이드워셜과 다르게 graph[k][i][j]는 한번만 계산되는 형태임.
            graph[k][i][j] = min(graph[k-1][i][j], graph[k-1][i][k] + graph[k-1][k][j])


for _ in range(Q):
    C, s, e = map(int, input().split())
    # C-1까지를 경유지로 삼았을때의 s-e 최단거리값이 INF라면 -1
    print(graph[C-1][s][e] if graph[C-1][s][e] != INF else -1)


# 답은 맞았으나 시간초과로 실패했던 코드들.
# 1) 다익스트라 사용
from sys import stdin
from heapq import heappop, heappush
from collections import defaultdict


input = stdin.readline
INF = int(1e9)

N, Q = map(int, input().split())
graph = defaultdict(dict)

for i in range(1, N+1):
    line = [0] + list(map(int, input().split()))
    for j in range(i+1, N+1):
        if line[j] == 0:
            continue
        graph[i][j] = line[j]
        graph[j][i] = line[j]


def dijkstra(start, end, limit):
    queue = []
    heappush(queue, (0, start, 0))
    visited = set()

    while queue:
        dist, curr, water = heappop(queue)

        if curr == end:
            return dist
        
        if (curr, water) in visited:
            continue

        visited.add((curr, water))

        for nxt in range(1, N+1):
            if graph[curr].get(nxt, -1) == -1:
                continue

            nxt_water = water
            if nxt != end:
                nxt_water = water + (1 << nxt)
            
            if nxt_water >= limit:
                continue

            nxt_dist = dist + graph[curr][nxt]
            heappush(queue, (nxt_dist, nxt, nxt_water))
    return -1


for _ in range(Q):
    C, s, e = map(int, input().split())
    limit = 1 << C

    print(dijkstra(s, e, limit))


# 2) 다익스트라 + DP + 비트마스킹
import sys
from heapq import heappop, heappush


input = sys.stdin.readline
INF = float("inf")

N, Q = map(int, input().split())
graph = [[INF] * (N+1) for _ in range(N+1)]

for i in range(1, N+1):
    line = [0] + list(map(int, input().split()))
    graph[i][i] = 0
    for j in range(i+1, N+1):
        if line[j] != 0:
            graph[i][j] = graph[j][i] = line[j]

def dijkstra(start, end, C):
    heap = [(0, start, 1 << start, 0)]
    dp = {}

    while heap:
        cost, curr, visited, dew = heappop(heap)

        if curr == end:
            return cost
        
        state = (curr, visited, dew)
        if state in dp and dp[state] < cost:
            continue

        for nxt in range(1, N+1):
            if visited & (1 << nxt) or graph[curr][nxt] == INF:
                continue

            new_visited = visited | (1 << nxt)
            new_cost = cost + graph[curr][nxt]
            new_dew = dew

            if nxt != end:
                new_dew += (1 << nxt)
                if new_dew >= (1 << C):
                    continue
            
            new_state = (nxt, new_visited, new_dew)
            if new_state not in dp or dp[new_state] > new_cost:
                dp[new_state] = new_cost
                heappush(heap, (new_cost, nxt, new_visited, new_dew))
    return -1


for _ in range(Q):
    C, s, e = map(int, input().split())
    print(dijkstra(s, e, C))