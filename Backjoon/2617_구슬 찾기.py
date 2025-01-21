# 문제집 - 0x18강 - 그래프


# 문제: https://www.acmicpc.net/problem/2617
# 메모리: 32412KB / 시간: 44ms
from sys import stdin


input = stdin.readline

N, M = map(int, input().split())

heavy = [[] for _ in range(N+1)]  # heavy[x] = [x보다 무거운 구슬]
light = [[] for _ in range(N+1)]  # light[x] = [x보다 가벼운 구슬]

for _ in range(M):
    h, l = map(int, input().split())
    heavy[h].append(l)
    light[l].append(h)


def dfs(graph: list, root: int) -> int:
    stack = [root]
    cnt = 0

    while stack:
        curr = stack.pop()
        for node in graph[curr]:
            if not visited[node]:
                visited[node] = True
                stack.append(node)
                cnt += 1
    return cnt


mid = (N+1) // 2
ret = 0

for root in range(1, N+1):
    visited = [False] * (N+1)

    # root보다 무거운 구슬이 mid개 이상 or 가벼운 구슬이 mid개 이상이라면 중간값 후보가 될 수 없음
    if dfs(heavy, root) >= mid:
        ret += 1
    if dfs(light, root) >= mid:
        ret += 1

print(ret)