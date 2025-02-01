# 문제집 - 0x1A강 - 위상 정렬


# 문제: https://www.acmicpc.net/problem/2623

# 싸이클을 탐지해야함.
# curr을 기준으로 싸이클을 탐지하면 X
"""
            if visited[curr]:
                if not finished[curr]:
                    return [0]
                continue

graph = {
    1: [2],
    2: [3],
    3: [4, 5],
    4: [3],  # 4 → 3 (사이클 경로)
    5: [6],
    6: [2]   # 6 → 2 (사이클 경로)
}

위와 같이 구성되어있을때, visited[curr]을 체크하면서 finished를 체크하는 방식을 사용하면 싸이클을 탐지할 수 없다.
"""
# 메모리: 32412KB / 시간: 36ms
from sys import stdin


input = stdin.readline

N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]

for _ in range(M):
    x, *line = map(int, input().split())
    if x == 0:
        continue
    for i in range(x-1):
        graph[line[i]].append(line[i+1])


def dfs():
    visited = [False] * (N+1)  # 방문 체크
    finished = [False] * (N+1)  # 처리가 끝난 노드 체크
    stack = []
    ret = []

    for i in range(1, N+1):
        if visited[i]:
            continue

        stack.append((i, False))

        while stack:
            curr, is_done = stack.pop()

            if is_done:  # 자식 노드를 모두 방문했다면 현재 노드 추가 후 처리했음을 체크
                finished[curr] = True
                ret.append(curr)
                continue

            if visited[curr]:
                continue

            visited[curr] = True
            stack.append((curr, True))

            for node in graph[curr]:
                if not visited[node]:
                    stack.append((node, False))
                elif not finished[node]:  # 만약 방문했지만 처리되지 않은 상태라면 싸이클
                    return [0]
    return ret[::-1]


print(*dfs(), sep="\n")