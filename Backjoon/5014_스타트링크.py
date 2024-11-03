# 문제집 - 0x09강 - BFS


# 문제: https://www.acmicpc.net/problem/5014
# S = 0, G = 0 인경우도 고려해야함.

# 메모리: 41424KB / 시간: 344ms
from sys import stdin
from collections import deque


input = stdin.readline
# S: 현재 강호가 있는층, G: 스타트링크, F: 전체 층수
F, S, G, U, D = map(int, input().split())

def bfs():
    queue = deque([(S, 0)])
    visited = [False] * (F+1)
    visited[S] = True

    while queue:
        x, time = queue.popleft()

        if x == G:
            return time
        
        for nx in (x + U, x - D):
            if 1 <= nx <= F and not visited[nx]:
                visited[nx] = True
                queue.append((nx, time + 1))
    return "use the stairs"

print(bfs())