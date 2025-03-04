# 문제집 - 0x1D강 - 다익스트라 알고리즘


# 문제: https://www.acmicpc.net/problem/24042

# 다시 풀어볼만한 문제 유형인듯.
# 메모리: 232892KB / 시간: 2948ms
from sys import stdin
from heapq import heappush, heappop


input = stdin.readline
INF = float("inf")


N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]

for i in range(M):
    A, B = map(int, input().split())
    graph[A].append((B, i))
    graph[B].append((A, i))


def dijkstra() -> int:
    times = [INF] * (N+1)
    times[1] = 0
    heap = [(0, 1)]

    while heap:
        time, curr = heappop(heap)

        if times[curr] < time:
            continue

        # time % M = 현재 주기에서 켜지는 횡단보도
        for nxt, t in graph[curr]:
            # 1. 신호가 아직 안왔거나 현재 시간과 타이밍이 정확히 맞을때
            if time % M <= t:
                wait_time = t - (time % M)
            # 2. 이미 지나가서 다음 신호를 기다려야할 때
            else:
                wait_time = M + t - (time % M) # 주기 + 이전 신호로부터 지난 시간(음수)
            
            new_time = time + wait_time
            if new_time + 1 < times[nxt]:  # 해당 신호가 켜지는시간 + 1(건너는 시간)
                times[nxt] = new_time + 1
                heappush(heap, (new_time+1, nxt))
    return times[N]


print(dijkstra())