# 최소 신장 트리


# n개의 별이 존재하며, n줄에 걸쳐 각 별의 x, y 좌표가 주어진다.
# 2차원 좌표가 아닌 1차원 좌표인줄 알고 헛수고했던 문제... (별1, 별2)로 주어지는 줄 알았다... 문제를 제대로 읽자...

# 4195_친구 네트워크 문제를 떠올리면 쉬운 문제다.
# parent, rank를 딕셔너리로 생성한다음, 각 별의 (x, y)를 키값으로 저장한다.

# 메모리: 32140KB / 시간: 48ms
from sys import stdin


input = stdin.readline

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(x, y):
    if x != y:
        if rank[x] < rank[y]:
            parent[x] = y
        elif rank[x] > rank[y]:
            parent[y] = x
        else:
            parent[y] = x
            rank[x] += 1

n = int(input())

parent, rank = {}, {}

stars = [tuple(map(float, input().split())) for _ in range(n)]  # 각 별들의 x, y 좌표
edges = []  # (별1, 별2, 두 별 사이의 거리)값들이 저장될 간선 리스트

# 각 별들끼리의 조합 생성
for i in range(n):
    for j in range(i):
        x1, y1 = stars[i]
        x2, y2 = stars[j]
        distance = (abs(x1-x2)**2 + abs(y1-y2)**2) ** 0.5
        edges.append(((x1, y1), (x2, y2), distance))
        
        # 별1 or 별2 가 parent에 없다면 x, y좌표를 키값으로 parent, rank에 추가해준다.
        if (x1, y1) not in parent:
            parent[(x1, y1)] = (x1, y1)
            rank[(x1, y1)] = 1
        
        if (x2, y2) not in parent:
            parent[(x2, y2)] = (x2, y2)
            rank[(x2, y2)] = 1

# 거리를 기준으로 오름차순 정렬
edges.sort(key=lambda x: x[2])

ret = 0.0  # 값이 실수형이므로 0.0으로 초기화
for s1, s2, dis in edges:
    s1, s2 = find(s1), find(s2)

    # 별1, 별2의 부모(집합)가 같지 않다면 동일화시켜준뒤 거리값을 누적한다.
    if s1 != s2:
        union(s1, s2)
        ret += dis

print(f"{ret:.2f}")  # 소수점 둘째자리까지만 출력