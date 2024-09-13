# 최소 신장 트리


# 첫번째 풀이. 제출하자마자 틀렸습니다.
from sys import stdin


input = stdin.readline

V, E = map(int, input().split())
graph = [tuple(map(int, input().split())) for _ in range(E)]

first = [False] * (V+1)
second = [False] * (V+1)

graph.sort(key=lambda x: x[2])

ret = 0
for u, v, w in graph:
    if not first[u] and not second[v]:
        first[u] = True
        second[v] = True
        ret += w

print(ret)

# 참고👉 https://velog.io/@yoopark/baekjoon-1197
# 메모리: 49216KB / 시간: 220ms
from sys import stdin


input = stdin.readline

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(a, b):
    if a != b:
        if rank[a] < rank[b]:
            parent[a] = b
        elif rank[a] > rank[b]:
            parent[b] = a
        else:
            parent[b] = a
            rank[a] += 1

V, E = map(int, input().split())
graph = [tuple(map(int, input().split())) for _ in range(E)]

parent = list(range(V+1))
rank = [0] * (V+1)

graph.sort(key=lambda x: x[2])

ret = 0
for u, v, w in graph:
    # find()함수로 u, v의 부모(집합)를 구한다음, 이 두 값이 같지 않을때에만 가중치를 ret에 더해준다.
    u, v = find(u), find(v)

    if u != v:
        union(u, v)
        ret += w

print(ret)