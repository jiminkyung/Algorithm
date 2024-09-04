# 트리


# 설명 참고👉 https://blogshine.tistory.com/111 => 트리의 지름을 구하는 원리
# 메모리: 76484KB / 시간: 512ms
from sys import stdin
from collections import deque


input = stdin.readline

def bfs(tree: list, start: int, v: int):
    queue = deque([(start, 0)])
    visited = [-1] * (v+1)
    visited[start] = 0
    ret_node = ret_dis = 0  # ret_node: start로부터 가장 먼 노드, ret_dis: 그 값

    while queue:
        curr_node, curr_dis = queue.popleft()
        
        for node, dis in tree[curr_node]:
            if visited[node] == -1:
                new_dis = dis + curr_dis
                visited[node] = new_dis
                queue.append((node, new_dis))

                if ret_dis < new_dis:  # 만약 새로운 거리값이 현재까지의 최대거리값보다 크다면 업데이트해준다.
                    ret_node = node
                    ret_dis = new_dis

    return ret_node, ret_dis


V = int(input())
tree = [[] for _ in range(V+1)]

for _ in range(V):
    ip = list(map(int, input().split()))
    node = ip[0]
    idx = 1
    while ip[idx] != -1:
        tree[node].append((ip[idx], ip[idx+1]))
        idx += 2

# 첫번째 bfs로 u를 구하고, 두번째 bfs로 v와 u-v거리를 구한다.
# 원의 아무곳에서 한 점을 찍고 제일 먼 거리를 구한값 = u, 그 값에서 가장 먼 거리인 값 = v 인 셈이다.
u, _ = bfs(tree, 1, V)
v, ret = bfs(tree, u, V)

print(ret)


# DFS로도 풀어보기? => 조금 더 빠르다.
# 메모리: 76520KB / 시간: 440ms
from sys import stdin


input = stdin.readline

def dfs(tree, start, v):
    stack = [(start, 0)]
    visited = [-1] * (v+1)
    visited[start] = 0
    ret_node = ret_dis = 0

    while stack:
        curr_node, curr_dis = stack.pop()
        visited[curr_node] = curr_dis

        for node, dis in tree[curr_node]:
            if visited[node] == -1:
                new_dis = dis + curr_dis
                stack.append((node, new_dis))
                if ret_dis < new_dis:
                    ret_node = node
                    ret_dis = new_dis
    return ret_node, ret_dis

V = int(input())
tree = [[] for _ in range(V+1)]

for _ in range(V):
    ip = list(map(int, input().split()))
    node = ip[0]
    idx = 1
    while ip[idx] != -1:
        tree[node].append((ip[idx], ip[idx+1]))
        idx += 2

u, _ = dfs(tree, 1, V)
v, ret = dfs(tree, u, V)

print(ret)