# 문제: https://school.programmers.co.kr/learn/courses/30/lessons/132266


# 플로이드 워셜로 풀어야 하나? 했으나 그냥 BFS로 가능한 문제.
# 출발점을 destination으로 잡고, sources까지의 거리값들을 저장하면 된다.
from collections import deque


def solution(n: int, roads: list[list[int]], sources: list[int], destination: int) -> list[int]:
    graph = [[] for _ in range(n)]

    for a, b in roads:
        graph[a-1].append(b-1)
        graph[b-1].append(a-1)


    def bfs():
        visited = [-1] * n
        visited[destination-1] = 0

        queue = deque([(destination-1, 0)])

        while queue:
            node, dist = queue.popleft()

            for nxt in graph[node]:
                if visited[nxt] == -1:
                    visited[nxt] = dist + 1
                    queue.append((nxt, dist + 1))
        
        ret = [visited[s-1] for s in sources]
        return ret
    

    return bfs()