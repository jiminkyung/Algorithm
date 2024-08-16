# 그래프와 순회

"""
BFS, DFS 모두 가능한 문제.
현재 노드와 인접한 노드들에 다른 색깔을 칠한다.(1 또는 -1)
이어지지 않는 두개의 이분 그래프가 주어질 수 있으므로, 주어진 그래프를 쭉 탐색해야함.
👇 반례
1
6 5
1 2
1 3
4 5
5 6
6 4

NO
"""


# BFS로 풀이
# 메모리: 51044KB / 시간: 1112ms
from sys import stdin


input = stdin.readline
K = int(input())

def bfs(start: int) -> bool:
    curr = [start]  # curr에 start를 집어넣고, 1로 색칠해준다.
    visited[start] = 1

    while curr:  # 같은 레벨의 노드들은 같은 색상을 갖게된다.
        nxt = []
        for i in curr:
            for j in graph[i]:  # 현재 노드의 인접 노드들을 탐색하며,
                if visited[j] == visited[i]:  # 현재 노드와 인접 노드의 색상이 같을경우 False를 반환한다.
                    return False
                if not visited[j]:  # 그렇지 않고 0인 상태(방문하지 않음)라면,
                    visited[j] = -visited[i]  # 현재 노드의 색상과 반대되는 색상을 할당한뒤 큐에 추가한다.
                    nxt.append(j)
        curr = nxt
    return True

for _ in range(K):
    V, E = map(int, input().split())
    graph = [[] for _ in range(V+1)]

    for _ in range(E):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)

    visited = [0] * (V+1)
    is_True = True

    for i in range(1, V+1):
        if not visited[i]:
            is_True = bfs(i)
            if not is_True:  # 동떨어진 이분 그래프 여러개가 주어질때, 하나라도 False라면 break 후 False 반환.
                break
    
    print("YES" if is_True else "NO")


# DFS로 풀이
# 메모리: 50940KB / 시간: 1088ms
from sys import stdin


input = stdin.readline
K = int(input())

def bfs(start):
    stack = [start]
    visited[start] = 1

    while stack:
        node = stack.pop()
        for i in graph[node]:
            if visited[i] == visited[node]:
                return False
            if not visited[i]:
                visited[i] = -visited[node]
                stack.append(i)
    return True

for _ in range(K):
    V, E = map(int, input().split())
    graph = [[] for _ in range(V+1)]

    for _ in range(E):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)

    visited = [0] * (V+1)
    is_True = True

    for i in range(1, V+1):
        if not visited[i]:
            is_True = bfs(i)
            if not is_True:
                break
    
    print("YES" if is_True else "NO")