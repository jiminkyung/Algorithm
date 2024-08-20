# 최단 경로

"""
- 무한회귀가 가능하다면 -1, 그 외에는 1부터 2, ... N번 정류장까지의 최단거리를 출력. 만약 갈 수 있는 경로가 없다면 -1 출력.
벨만-포드 알고리즘을 사용해야 하는 문제다.
단순히 음수 가중치만 있는 경우 다익스트라 알고리즘을 사용해도 무방하나,
음수 그래프가 존재한다면(무한히 작아짐) 다익스트라 알고리즘은 무한반복에 빠지게된다.
"""


# 다익스트라 알고리즘을 사용했던 풀이. => 실패! 무한반복!
from sys import stdin
import heapq


input = stdin.readline
N, M = map(int, input().split())
stop = [[] for _ in range(N+1)]

for _ in range(M):
    A, B, C = map(int, input().split())
    stop[A].append((B, C))

def dijkstra():
    times = [int(1e9)] * (N+1)
    times[1] = 0
    heap = [(0, 1)]

    while heap:
        curr_time, curr_node = heapq.heappop(heap)

        if curr_time > times[curr_node]:
            continue

        for s, t in stop[curr_node]:
            new_time = curr_time + t
            if new_time < times[s]:
                times[s] = new_time
                heapq.heappush(heap, (new_time, s))
    return times

ret = []
ret_times = dijkstra()

for i in range(2, N+1):
    if ret_times[i] >= int(1e9):
        ret.append(-1)
    else:
        ret.append(ret_times[i])

if ret_times[N] < 0:
    print("-1")
else:
    print(*ret, sep="\n")


# 벨만-포드 알고리즘으로 작성
# 메모리: 32140KB / 시간: 400ms
from sys import stdin


input = stdin.readline
N, M = map(int, input().split())
INF = int(1e9)
stop = []

for _ in range(M):
    stop.append(tuple(map(int, input().split())))  # (A, B, C)형태로 추가

def bellman_ford():
    times = [INF] * (N+1)
    times[1] = 0

    for _ in range(N-1):  # 노드수-1 만큼 반복
        for u, v, w in stop:  # u -> v, w는 가중치다.
            if times[u] != INF and times[u] + w < times[v]:  # 만약 현재 노드가 INF가 아니고, 현재 노드의 경로값 + 노드 v까지의 가중치 < 노드 v의 경로값이라면,
                times[v] = times[u] + w  # 노드 v의 경로값을 현재 노드의 경로값 + v까지의 가중치 로 변경한다.
    
    # 음수 사이클 유무 확인하기 -> 만약 변경되는 값이 있다면 음수 사이클이 있다는것이므로 False를 반환해준다.
    for u, v, w in stop:
        if times[u] != INF and times[u] + w < times[v]:
            return False
    
    return times  # 음수 사이클이 발견되지 않았다면 최단경로리스트 times를 반환한다.

ret = bellman_ford()

if not ret:
    print(-1)
else:
    for i in range(2, N+1):
        print(ret[i] if ret[i] != INF else -1)