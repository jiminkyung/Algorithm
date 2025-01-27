# 문제집 - 0x19강 - 트리


# 문제: https://www.acmicpc.net/problem/14267

# 칭찬을 받을때마다 DFS를 실행하면 시간초과
# 칭찬 포인트를 기록해뒀다가 한번에 실행해야 통과됨
# 메모리: 56556KB / 시간: 212ms
from sys import stdin


input = stdin.readline

N, M = map(int, input().split())
parent = [0] + list(map(int, input().split()))
child = [[] for _ in range(N+1)]
point = [0] * (N+1)

# 자식노드들 저장
for i in range(2, N+1):
    child[parent[i]].append(i)

def dfs():
    stack = [(1, 0)]  # 사장은 칭찬받을일 없음

    while stack:
        curr, pt = stack.pop()
        
        for c in child[curr]:
            point[c] += pt  # 현재까지의 칭찬 포인트에 상사로부터 전달된 포인트 추가
            stack.append((c, point[c]))  # 자식들에게 칭찬 물려주기


for _ in range(M):
    i, w = map(int, input().split())
    point[i] += w


dfs()
print(*point[1:])