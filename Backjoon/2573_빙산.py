# 문제집 - 0x09강 - BFS


# 문제: https://www.acmicpc.net/problem/2573
# 2636_치즈 와 비슷한 문제.

# 메모리: 34104KB / 시간: 2628ms
from sys import stdin
from collections import deque


input = stdin.readline

def bfs(x, y):
    queue = deque([(x, y)])
    visited[x][y] = True
    sea = []

    while queue:
        cx, cy = queue.popleft()
        s = 0  # pole[cx][cy] 주변 바다의 갯수
        for dx, dy in directions:
            nx, ny = dx + cx, dy + cy
            if 0 <= nx < N and 0 <= ny < M:
                if pole[nx][ny] == 0:
                    s += 1
                elif pole[nx][ny] != 0 and not visited[nx][ny]:
                    visited[nx][ny] = True
                    queue.append((nx, ny))
        if s > 0:
            sea.append((cx, cy, s))
    
    for x, y, s in sea:
        pole[x][y] = max(0, pole[x][y] - s)  # 최솟값은 0이 되어야 한다.
    return 1


N, M = map(int, input().split())
pole = [list(map(int, input().split())) for _ in range(N)]
directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
year = 0

while True:
    visited = [[False] * M for _ in range(N)]
    cnt = 0  # 덩어리의 갯수
    for i in range(N):
        for j in range(M):
            if pole[i][j] != 0 and not visited[i][j]:
                cnt += bfs(i, j)
    if cnt == 0:  # 다 녹을때까지 덩어리가 2개 이상이 되지 않는다면 0 출력
        print(0)
        break
    if cnt >= 2:
        print(year)
        break
    year += 1