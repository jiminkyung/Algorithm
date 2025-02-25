# 문제집 - 0x1B강 - 최소 신장 트리


# 문제: https://www.acmicpc.net/problem/2887

"""
모든 행성 쌍 간의 간선을 생성하면 메모리 초과 발생!
- 비용 함수가 min(|x1-x2|, |y1-y2|, |z1-z2|)임.
- ⭐ 각 축별로 정렬하고 인접한 행성끼리만 연결해도 MST를 찾을 수 있음.
    -> x축 정렬 후 x차이, y축 정렬 후 y차이, z축 정렬 후 z차이를 비용으로 사용.
    -> 이렇게 해서 총 3*(N-1)개의 간선만 고려하면 됨.
    -> 전체 MST의 간선 (N-1)개는 이 안에 포함됨.
- 멀리 떨어진 행성보다 중간에 있는 행성들 거쳐가는게 더 효율적이라는 원리다.
- 각 축별 간선 모아서 크루스칼 알고리즘 적용하면 끝.

질문 게시판에 어떤분이 남기신 해석글이 있다... 나중에 헷갈리면 다시 보자.
참고: https://www.acmicpc.net/board/view/145011
"""

# 메모리: 90500KB / 시간: 1300ms
from sys import stdin


input = stdin.readline

N = int(input())
planets = []

# 각 행성의 좌표와 원래 인덱스 저장
for idx in range(N):
    x, y, z = map(int, input().split())
    planets.append((x, y, z, idx))


def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(a, b):
    a, b = find(a), find(b)

    if a != b:
        if a < b:
            parent[b] = a
        else:
            parent[a] = b
        return True
    return False


MST = []

# x, y, z 순서대로 정렬
for i in range(3):
    planets.sort(key=lambda x: x[i])
    for j in range(N-1):
        a, b = planets[j], planets[j+1]
        MST.append((abs(a[i]-b[i]), a[3], b[3]))


# 비용 기준 정렬 후 크루스칼 알고리즘 시행
parent = list(range(N))
MST.sort()  # 🚨 sort(key=lambda x: x[0])으로 정렬하면 메모리 사용량은 커지지만 실행시간은 300ms정도 줄어듬.
total_cost = edge_cnt = 0

for cost, a, b in MST:
    if union(a, b):
        total_cost += cost
        edge_cnt += 1
    
    if edge_cnt == N-1:  # 최소 간선을 생성했다면 break
        break

print(total_cost)