# 트리


# BFS 방식으로 탐색해보기.
# 메모리: 48044KB / 시간: 316ms
from sys import stdin


input = stdin.readline

N = int(input())
tree = [[] for _ in range(N+1)]

for _ in range(N-1):
    u, v = map(int, input().split())
    # 양방향이므로 각각 저장해줘야 한다.
    tree[u].append(v)
    tree[v].append(u)

# parent[i] = 노드 i의 부모 노드
parent = [-1] * (N+1)

curr = [1]
parent[1] = 0  # 1의 부모 노드는 0으로 설정한 뒤 탐색 시작.

while curr:
    nxt = []  # 다음 레벨의 노드들
    for i in curr:
        for j in tree[i]:
            # 부모가 없는 상태일 때, 현재값(i)를 저장한 뒤 탐색할 노드리스트에 저장.
            if parent[j] == -1:
                parent[j] = i
                nxt.append(j)
    curr = nxt

for i in range(2, N+1):
    print(parent[i])


# dfs로 풀어도 가능. 어느 방식이든지 상관없음.
# 메모리: 49068KB / 시간: 284ms
from sys import stdin


input = stdin.readline

N = int(input())
tree = [[] for _ in range(N+1)]

for _ in range(N-1):
    u, v = map(int, input().split())
    tree[u].append(v)
    tree[v].append(u)

parent = [-1] * (N+1)
parent[1] = 0

stack = [1]

while stack:
    curr = stack.pop()

    for node in tree[curr]:
        if parent[node] == -1:
            parent[node] = curr
            stack.append(node)

for i in range(2, N+1):
    print(parent[i])