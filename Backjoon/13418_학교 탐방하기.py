# 문제집 - 0x1B강 - 최소 신장 트리


# 문제: https://www.acmicpc.net/problem/13418

# 프림 알고리즘으로 통과했지만, 크루스칼로 푸는게 훨씬 효율적임.
# => 어차피 가중치 값은 1, 0 뿐이므로 따로 정렬해 줄 필요 없이 한번에 처리할 수 있음.

# 1. 프림 알고리즘 풀이
# 메모리: 202628KB / 시간: 1768ms
"""
문제에서 오르막은 0, 내리막은 1임.
기존 프림 알고리즘대로 작성 후 실행시키면 비효율적인 길만 찾아서 가게 됨.
즉,

첫 prim 실행
- 오르막: 0, 내리막: 1
- cnt: 내리막길의 수
- N - cnt: 오르막길의 수
- worst값: (N - cnt) ** 2

그리고 (1 - 기존값)을 통해 오르막/내리막을 반전시킴.

두번째 prim 실행
- 오르막: 1, 내리막: 0
- cnt: 오르막길의 수
- best값: cnt ** 2
"""
from sys import stdin


input = stdin.readline

N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]

for _ in range(M+1):
    A, B, C = map(int, input().split())
    graph[A].append((B, C))
    graph[B].append((A, C))


def prim():
    values = [float("inf")] * (N+1)
    visited = [False] * (N+1)
    values[0] = 0
    cnt = 0

    for _ in range(N+1):
        min_node = -1
        min_val = float("inf")

        for i in range(N+1):
            if not visited[i] and values[i] < min_val:
                min_node = i
                min_val = values[i]

        visited[min_node] = True
        cnt += min_val

        for nxt, val in graph[min_node]:
            if visited[nxt] or values[nxt] <= val:
                continue
            values[nxt] = val
    
    return cnt


worst = (N - prim()) ** 2

# 1, 0 반전시키기
graph = [[(node, 1 - val) for node, val in graph[i]] for i in range(N+1)]
best = prim() ** 2

print(worst - best)


# ⭐ 2. 크루스칼 알고리즘 풀이
# 메모리: 91776KB / 시간: 720ms
from sys import stdin


input = stdin.readline

N, M = map(int, input().split())
graph = [tuple(map(int, input().split())) for _ in range(M+1)]

b_parent = list(range(N+1))
w_parent = list(range(N+1))

# 비교값이 1과 0밖에 없으므로 따로 정렬해 줄 필요 ❌
def find(x, parent):
    if parent[x] != x:
        parent[x] = find(parent[x], parent)
    return parent[x]

def union(a, b, parent):
    a = find(a, parent)
    b = find(b, parent)

    if a != b:
        if parent[a] < parent[b]:
            parent[b] = a
        else:
            parent[a] = b
        return True
    return False


best, worst = N, 0

for A, B, C in graph:
    # 내리막길 = 최적
    if C == 1:
        if union(A, B, b_parent):
            best -= 1
    # 오르막길 = 최악
    else:
        if union(A, B, w_parent):
            worst += 1


print(worst ** 2 - best ** 2)