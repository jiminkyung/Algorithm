# 문제집 - 0x09강 - BFS


# 문제: https://www.acmicpc.net/problem/5427
# 4179_불! 에서 변형된 문제.(한가지 케이스 -> 여러개의 케이스)

# 메모리: 107724KB / 시간: 1860ms
from sys import stdin
from collections import deque


input = stdin.readline

def bfs():
    while queue_f:
        x, y = queue_f.popleft()
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < h and 0 <= ny < w:
                if visited_f[nx][ny] == 0:
                    visited_f[nx][ny] = visited_f[x][y] + 1
                    queue_f.append((nx, ny))
    
    while queue_s:
        x, y = queue_s.popleft()
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < h and 0 <= ny < w:
                if visited_s[nx][ny] != 0:
                    continue
                if visited_f[nx][ny] == 0 or visited_f[nx][ny] > visited_s[x][y] + 1:
                    visited_s[nx][ny] = visited_s[x][y] + 1
                    queue_s.append((nx, ny))
            else:
                return visited_s[x][y]
    
    return "IMPOSSIBLE"


directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

for _ in range(int(input())):
    w, h = map(int, input().split())

    queue_s = deque([])
    queue_f = deque([])

    visited_s = [[0] * w for _ in range(h)]
    visited_f = [[0] * w for _ in range(h)]

    building = []

    for i in range(h):
        line = input().rstrip()
        for j in range(w):
            if line[j] == "#":
                visited_f[i][j] = 1
                visited_s[i][j] = 1
            elif line[j] == "@":
                queue_s.append((i, j))
                visited_s[i][j] = 1
            elif line[j] == "*":
                queue_f.append((i, j))
                visited_f[i][j] = 1
    print(bfs())