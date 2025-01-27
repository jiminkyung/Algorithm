# 문제집 - 0x19강 - 트리


# 문제: https://www.acmicpc.net/problem/20955

# 유니온-파인드를 사용하여 풀이
# 메모리: 56512KB / 시간: 212ms
from sys import stdin


input = stdin.readline

N, M = map(int, input().split())

edges = [tuple(map(int, input().split())) for _ in range(M)]
parent = list(range(N+1))


def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(a, b):
    a, b = find(a), find(b)

    # 아직 연결되지 않은 간선이라면 True, 연결되어 있는 간선(=싸이클)이라면 False
    if a != b:
        if a < b:
            parent[b] = a
        else:
            parent[a] = b
        return True
    return False


ret = 0  # 필요한 연산의 수 = 트리끼리 연결하는 횟수 + 제거할 간선의 수(싸이클)

for u, v in edges:
    ret += not union(u, v)  # 싸이클일경우 1

group = set(find(i) for i in range(1, N+1))  # 그룹의 갯수
ret += len(group) - 1

print(ret)


# 더 간단한 계산법! https://www.acmicpc.net/source/89102456
"""
N-1 = N개의 노드를 트리로 구성하기위한 간선의 수
cnt = 성공적으로 연결된 간선의 수
res = 제거해야할 간선의 수

    for _ in range(M):
        u, v = map(int, input().split())
        if find(u) != find(v):
            union(u, v)
            cnt += 1
        else:
            res += 1
    print((N-1) - cnt + res)
"""