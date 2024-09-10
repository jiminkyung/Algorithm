# 유니온 파인드


# 메모리: 31120KB / 시간: 48ms
from sys import stdin


input = stdin.readline

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(a, b):
    a, b = find(a), find(b)
    
    if a != b:
        if rank[a] < rank[b]:
            parent[a] = b
        elif rank[a] > rank[b]:
            parent[b] = a
        else:
            parent[b] = a
            rank[a] += 1

N = int(input())
M = int(input())

parent = list(range(N+1))
rank = [0] * (N+1)

path = [list(map(int, input().split())) for _ in range(N)]

for i in range(N):
    for j in range(N):
        if path[i][j] == 1:
            union(i+1, j+1)

goal = list(map(int, input().split()))
ret = parent[goal[0]]  # 같은 집합안에 있다면, 모두 같은 parent값일것이다.

for i in range(1, M):
    if ret != parent[goal[i]]:
        print("NO")
        break
else:
    print("YES")


# 랭크 없는 버전
# 메모리: 31120KB / 시간: 40ms
from sys import stdin


input = stdin.readline

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(a, b):
    a, b = find(a), find(b)
    
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

N = int(input())
M = int(input())

parent = list(range(N+1))
path = [list(map(int, input().split())) for _ in range(N)]

for i in range(N):
    for j in range(N):
        if path[i][j] == 1:
            union(i+1, j+1)

goal = list(map(int, input().split()))
ret = parent[goal[0]]

for i in range(1, M):
    if ret != parent[goal[i]]:
        print("NO")
        break
else:
    print("YES")