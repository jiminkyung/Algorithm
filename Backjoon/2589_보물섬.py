# 문제집 - 대학생 기본반


# 문제: https://www.acmicpc.net/problem/2589
# 메모리: 34072KB / 시간: 4264ms
from sys import stdin
from collections import deque


input = stdin.readline

def bfs(x, y):
    global ret
    queue = deque([(x, y, 0)])
    visited = [[False] * n for _ in range(m)]
    visited[x][y] = True

    while queue:
        cx, cy, dis = queue.popleft()
        ret = max(ret, dis)

        for nx, ny in ((cx-1, cy), (cx+1, cy), (cx, cy-1), (cx, cy+1)):
            if nx < 0 or nx >= m or ny < 0 or ny >= n:
                continue

            if not visited[nx][ny] and MAP[nx][ny] == "L":
                visited[nx][ny] = True
                queue.append((nx, ny, dis + 1))


m, n = map(int, input().split())
MAP = [input().rstrip() for _ in range(m)]

ret = 0

for i in range(m):
    for j in range(n):
        if MAP[i][j] == "L":
            bfs(i, j)

print(ret)


# 실행시간 384ms인 풀이! 더 빠른 풀이도 있었지만 가독성이 떨어짐.
# 모든 "L"에 대해서 bfs를 실행하지 않고,
# 해당 "L"의 상하 또는 좌우에 "L"이 존재한다면 pass하는 형식이다.
from collections import deque
import sys
input = sys.stdin.readline


def bfs(r,c):

    dist = [[0] * m for _ in range(n)]
    dr = [-1,1,0,0]
    dc = [0,0,-1,1]

    visited[r][c] = True

    queue = deque()
    queue.append((r,c))

    while queue:

        r, c = queue.popleft()

        for d in range(4):
            nr = r + dr[d]
            nc = c + dc[d]
            if 0 <= nr < n and 0 <= nc < m and board[nr][nc] == 'L' and not visited[nr][nc]:
                dist[nr][nc] = dist[r][c] + 1
                visited[nr][nc] = True
                queue.append((nr,nc))


    return max(map(max,dist))


n, m = map(int,input().split())
board = [list(input().strip()) for _ in range(n)]

answer = 0
for i in range(n):
    for j in range(m):
        if board[i][j] == 'L':
            visited = [[False] * m for _ in range(n)]
            if 0 <= i - 1 and i + 1 < n:
                if board[i - 1][j] == 'L' and board[i + 1][j] == 'L':
                    continue
            if 0 < j - 1 and j + 1 < m:
                if board[i][j - 1] == 'L' and board[i][j - 1] == 'L':
                    continue
            answer = max(answer, bfs(i, j))

print(answer)