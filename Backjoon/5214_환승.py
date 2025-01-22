# 문제집 - 0x18강 - 그래프


# 문제: https://www.acmicpc.net/problem/5214

# 역의 정보만 저장해서 풀었더니 메모리초과.
# 역과 하이퍼튜브를 양방향으로 연결해서 풀어야함.

# 메모리: 97712KB / 시간: 820ms
from sys import stdin
from collections import deque


input = stdin.readline

N, K, M = map(int, input().split())
# 1 ~ N: 역, N+1 ~ M: 하이퍼튜브
graph = [[] for _ in range(N+1+M)]

for i in range(1, M+1):
    stations = map(int, input().split())
    tube = N + i  # 하이퍼튜브 번호

    # 역 <-> 하이퍼튜브 양방향 연결
    # 예를들어 1번역과 3번 하이퍼튜브가 연결되어있고, N번역도 3번 하이퍼튜브와 연결되어있다면
    # 1번역 -> 3번튜브 -> N번역 이런식으로 움직일 수 있게끔
    for station in stations:
        graph[station].append(tube)
        graph[tube].append(station)


def bfs():
    queue = deque([(1, 1)])
    visited = [False] * (N+1+M)
    visited[1] = True

    while queue:
        curr, dis = queue.popleft()

        if curr == N:
            return dis
        
        for nxt in graph[curr]:
            if not visited[nxt]:
                visited[nxt] = True

                # nxt가 역인 경우에만 거리 1 증가
                if nxt <= N:
                    queue.append((nxt, dis+1))
                else:
                    queue.append((nxt, dis))
    return -1


print(bfs())