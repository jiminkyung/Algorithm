# 문제집 - 0x1B강 - 최소 신장 트리


# 문제: https://www.acmicpc.net/problem/16398

# 크루스칼 알고리즘으로 풀이. 하지만 프림 알고리즘을 사용하는것이 더 유리한 문제다.
# => 모든 간선의 정보가 주어지기 때문인듯.

# 1. 크루스칼 알고리즘 풀이
# 메모리: 102560KB / 시간: 948ms
from sys import stdin


input = stdin.readline

N = int(input())
graph = []
parent = list(range(N))

for i in range(N):
    line = list(map(int, input().split()))
    # 주대각선(자기 자신) 전까지만 체크
    for j in range(i):
        graph.append((i, j, line[j]))

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]


def union(a, b):
    a, b = find(a), find(b)

    if a != b:
        if parent[a] < parent[b]:
            parent[b] = a
        else:
            parent[a] = b
        return True
    return False


graph.sort(key=lambda x: x[2])
ret = 0

for u, v, w in graph:
    # 같은 집합이 아니라면 결과값에 비용 추가
    if union(u, v):
        ret += w

print(ret)


# 2. 프림 알고리즘 풀이 (heapq 사용)
# 메모리: 74296KB / 시간: 392ms
from sys import stdin
from heapq import heappush, heappop


input = stdin.readline

N = int(input())
graph = [tuple(map(int, input().split())) for _ in range(N)]
distance = [float("inf")] * N  # 현재까지 만들어진 MST와 연결될 수 있는 최소 비용
visited = [False] * N

ret = cnt = 0
heap = [(0, 0)]

while heap:
    cost, node = heappop(heap)

    if visited[node]:  # 이미 방문한 노드라면 패스
        continue

    visited[node] = True
    ret += cost
    cnt += 1
    
    # 카운팅한 노드의 갯수가 N개라면 break
    if cnt >= N:
        break

    # 다음 노드의 번호, 비용
    for nxt, cost in enumerate(graph[node]):
        if visited[nxt] or distance[nxt] <= cost:  # 이미 방문한 노드거나 최솟값이 cost보다 작다면 넘어간다.
            continue
        heappush(heap, (cost, nxt))
        distance[nxt] = cost


print(ret)


# 3. 프림 알고리즘 풀이 (리스트 사용)
# 메모리: 71096KB / 시간: 504ms
from sys import stdin


input = stdin.readline

N = int(input())
graph = [tuple(map(int, input().split())) for _ in range(N)]
distance = [float("inf")] * N  # MST에 포함된 노드들로부터 각 노드까지의 최소 연결비용
visited = [False] * N

# 0번째 노드의 값을 0으로 설정 후 MST 생성 시작
distance[0] = 0
ret = 0

# 모든 노드를 MST에 포함시킬때까지 반복
for _ in range(N):
    # 현재 MST에 연결할 수 있는 가장 작은 비용의 노드를 찾아야함.
    min_dis = float("inf")
    min_node = -1

    for i in range(N):
        if not visited[i] and distance[i] < min_dis:
            min_dis = distance[i]
            min_node = i
    
    # MST에 포함시킨 뒤 결과값에 비용 추가
    visited[min_node] = True
    ret += min_dis

    # 새로 추가된 노드로부터 다른 노드들까지의 최소 연결 비용 갱신
    for nxt in range(N):
        if visited[nxt] or distance[nxt] <= graph[min_node][nxt]:
            continue
        distance[nxt] = graph[min_node][nxt]


print(ret)