# 유니온 파인드


# 유니온 파인드 문제 자체를 처음 풀어봐서 감이 안잡혔다...
# 경로 압축 기법이 주로 쓰이는 듯 하다.

# 참고👉 https://velog.io/@dhelee/%EB%B0%B1%EC%A4%80-1717%EB%B2%88-%EC%A7%91%ED%95%A9%EC%9D%98-%ED%91%9C%ED%98%84-Python-%EC%9E%90%EB%A3%8C%EA%B5%AC%EC%A1%B0
# 메모리: 76584KB / 시간: 272ms
import sys


input = sys.stdin.readline
sys.setrecursionlimit(10**9)

def find(x):  # 경로 압축(Path Compression) 방식
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(a, b):
    a, b = find(a), find(b)

    if a < b:  # 큰값의 부모를 작은값으로 설정
        parent[b] = a
    else:
        parent[a] = b

n, m = map(int, input().split())
parent = [i for i in range(n+1)]

for _ in range(m):
    cmd, a, b = map(int, input().split())

    if cmd == 0:
        union(a, b)
    else:
        print("YES" if find(a) == find(b) else "NO")


# 랭크를 사용하는 방식. 대규모 데이터가 주어졌을때 추천하는 방식이라고 한다. (트리의 높이를 최소화)
# 즉, 랭크 = 각 노드를 루트로 하는 트리의 "높이" 인 셈이다.

# 메모리: 78492KB / 시간: 280ms
import sys
input = sys.stdin.readline

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(x, y):
    x = find(x)
    y = find(y)
    if x != y:
        if rank[x] < rank[y]:
            parent[x] = y
        elif rank[x] > rank[y]:
            parent[y] = x
        else:
            parent[y] = x
            rank[x] += 1

n, m = map(int, input().split())
parent = list(range(n + 1))
rank = [0] * (n + 1)

for _ in range(m):
    op, a, b = map(int, input().split())
    if op == 0:
        union(a, b)
    else:
        if find(a) == find(b):
            print("YES")
        else:
            print("NO")