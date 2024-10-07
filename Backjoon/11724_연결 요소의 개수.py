# 문제집 - 대학생 기본반


# 문제: https://www.acmicpc.net/problem/11724
# 메모리: 65164KB / 시간: 584ms
from sys import stdin


input = stdin.readline

def bfs(start):
    curr = [start]
    visited[start] = True

    while curr:
        nxt = []
        for node in curr:
            for v in graph[node]:
                if not visited[v]:
                    visited[v] = True
                    nxt.append(v)
        curr = nxt
    return 1

N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]

for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

visited = [False] * (N+1)
ret = 0

for i in range(1, N+1):
    if not visited[i]:
        ret += bfs(i)

print(ret)


# 그냥 딕셔너리 + 유니온 파인드로 푼 사람도 있는듯하다? 한번 풀어보자.
# 참고👉 https://www.acmicpc.net/source/39701069
# 메모리: 31120KB / 시간: 448ms
from sys import stdin


input = stdin.readline

def union(a, b):
    a, b = parent[a], parent[b]

    if a != b:
        if a > b:
            a, b = b, a
        
        for n in network[b]:
            parent[n] = a
            network[a].append(n)
        del network[b]

N, M = map(int, input().split())
parent = {i: i for i in range(1, N+1)}
network = {i: [i] for i in range(1, N+1)}

for _ in range(M):
    u, v = map(int, input().split())
    union(u, v)

print(len(network))