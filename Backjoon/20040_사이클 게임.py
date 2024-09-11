# 유니온 파인드


# 제출용
# 메모리: 54292KB / 시간: 560ms
from sys import stdin


input = stdin.readline

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(a, b, cnt):
    a, b = find(a), find(b)

    if a == b:
        return cnt
    
    if rank[a] < rank[b]:
        parent[a] = b
    elif rank[b] < rank[a]:
        parent[b] = a
    else:
        parent[b] = a
        rank[a] += 1
    return 0

n, m = map(int, input().split())

parent = list(range(n))
rank = [0] * n

ret = 0

for i in range(1, m+1):
    a, b = map(int, input().split())
    cnt = union(a, b, i)

    if cnt:
        ret = cnt
        break

print(ret)


# vscode용(입력값 끝까지 받기)
# 메모리: 190544KB / 시간: 1108ms
from sys import stdin


input = stdin.readline

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(a, b, cnt):
    a, b = find(a), find(b)

    if a == b:
        return cnt
    
    if rank[a] < rank[b]:
        parent[a] = b
    elif rank[b] < rank[a]:
        parent[b] = a
    else:
        parent[b] = a
        rank[a] += 1
    return 0

n, m = map(int, input().split())

edge = [tuple(map(int, input().split())) for _ in range(m)]

parent = list(range(n))
rank = [0] * n

ret = 0

for i, (a, b) in enumerate(edge, start=1):
    cnt = union(a, b, i)

    if cnt:
        ret = cnt
        break

print(ret)


# 실행시간 440ms인 코드.
# 단일 배열로 집합의 구조와 크기를 표현.
# 합칠 때는 큰 집합에 작은 집합을 연결하고 찾을 때는 경로를 압축하여 최적화한다.
import sys
input = sys.stdin.readline
print = sys.stdout.write

def find(x):
    if parent[x] < 0: return x
    parent[x] = find(parent[x])
    return parent[x]

def union(x, y):
    if parent[x] < parent[y]:
        parent[y] = x
    else:
        if parent[x] == parent[y]:
            parent[y] -= 1
        parent[x] = y

def solve():
    for i in range(m):
        u, v = map(int, input().split())
        uset, vset = find(u), find(v)
        if uset == vset: return str(i+1)
        union(uset, vset)
    return '0'

n, m = map(int, input().split())
parent = [-1]*n
print(solve())