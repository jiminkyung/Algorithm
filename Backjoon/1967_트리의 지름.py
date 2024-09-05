# 트리


# 트리 => 사이클이 없는 그래프 이므로 가중치가 있어도 BFS로 풀 수 있음.
# 1167_트리의 지름 문제와 유사함.

# 메모리: 34536KB / 시간: 68ms
from sys import stdin
from collections import deque


input = stdin.readline

def bfs(tree, start, v):
    queue = deque([(start, 0)])
    visited = [False] * (v+1)  # 경로값을 저장할 필요는 없으므로 boolean값으로 초기화한다.
    visited[start] = True
    ret_node = ret_dis = 0

    while queue:
        curr_node, curr_dis = queue.popleft()

        for node, dis in tree[curr_node]:
            if not visited[node]:
                new_dis = dis + curr_dis
                visited[node] = True
                queue.append((node, new_dis))

                if ret_dis < new_dis:
                    ret_node = node
                    ret_dis = new_dis
    
    return ret_node, ret_dis

V = int(input())
tree = [[] for _ in range(V+1)]

for _ in range(V-1):
    u, v, w = map(int, input().split())
    tree[u].append((v, w))
    tree[v].append((u, w))  # bfs()를 여러번 실행해야 하므로 양방향 저장

u, _ = bfs(tree, 1, V)
v, ret = bfs(tree, u, V)

print(ret)


# DFS 사용 풀이. 더 빠르다.
# 메모리: 34188KB / 시간: 48ms
from sys import stdin


input = stdin.readline

def bfs(tree, start, v):
    stack = [(start, 0)]
    visited = [False] * (v+1)
    visited[start] = True
    ret_node = ret_dis = 0

    while stack:
        curr_node, curr_dis = stack.pop()
        visited[curr_node] = True

        for node, dis in tree[curr_node]:
            if not visited[node]:
                new_dis = dis + curr_dis
                stack.append((node, new_dis))

                if ret_dis < new_dis:
                    ret_node = node
                    ret_dis = new_dis
    
    return ret_node, ret_dis

V = int(input())
tree = [[] for _ in range(V+1)]

for _ in range(V-1):
    u, v, w = map(int, input().split())
    tree[u].append((v, w))
    tree[v].append((u, w))

u, _ = bfs(tree, 1, V)
v, ret = bfs(tree, u, V)

print(ret)