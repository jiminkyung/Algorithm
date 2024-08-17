# 최단 경로

"""
다익스트라 알고리즘:
    - 그래프에서 한 정점에서 다른 모든 정점까지의 최단 경로를 찾는 알고리즘
    - 음의 가중치가 없는 그래프에서 사용 가능
    - 그리디 알고리즘의 일종으로, 항상 가장 비용이 적은 노드를 선택하여 탐색

알고리즘 동작 과정:
    1. 시작 노드를 설정하고, 시작 노드의 거리를 0으로, 나머지 노드의 거리를 무한대로 초기화
    2. 방문하지 않은 노드 중 최단 거리가 가장 짧은 노드를 선택
    3. 해당 노드를 거쳐 다른 노드로 가는 비용을 계산하여, 더 짧은 경로가 있다면 갱신
    4. 2-3 과정을 모든 노드를 방문할 때까지 반복

우선순위 큐(heapq)를 사용하여 효율성을 높임.
"""

# 메모리: 68508KB / 시간: 580ms

from sys import stdin
import heapq

input = stdin.readline
V, E = map(int, input().split())
K = int(input())

graph = [[] for _ in range(V+1)]

for _ in range(E):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))

ret = [float("inf")] * (V+1)

def dijkstra(start):
    ret[start] = 0
    queue = [(0, start)]

    while queue:
        curr_dis, curr_node = heapq.heappop(queue)

        # 현재 노드까지의 거리가 기존에 계산된 거리보다 크다면 무시한다.
        if curr_dis > ret[curr_node]:
            continue

        # 현재 노드와 연결된 다른 인접한 노드들을 확인
        for v, w in graph[curr_node]:
            new_dis = curr_dis + w
            # 현재 노드를 거쳐서 다른 노드로 이동하는 거리가 더 짧은 경우,
            if new_dis < ret[v]:
                ret[v] = new_dis  # 해당 거리값을 현재 노드-다른 노드 이동 거리값으로 변경한다.
                heapq.heappush(queue, (new_dis, v))  # 그리고 힙에 (거리, 노드)형태로 튜플 추가.

dijkstra(K)

for i in range(1, V+1):
    print("INF" if ret[i] == float("inf") else ret[i])