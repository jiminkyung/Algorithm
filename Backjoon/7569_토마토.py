# 그래프와 순회

# 메모리: 48492KB / 시간: 1552ms

from sys import stdin
from collections import deque


input = stdin.readline
M, N, H = map(int, input().split())  # M: 열, N: 행, H: 높이
box = [[list(map(int, input().split())) for _ in range(N)] for _ in range(H)]
tomato = deque([])

for i in range(H):
    for j in range(N):
        for k in range(M):
            if box[i][j][k] == 1:
                tomato.append((i, j, k))

directions = [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]

def bfs():
    while tomato:
        x, y, z = tomato.popleft()
        for dx, dy, dz in directions:
            nx, ny, nz = x + dx, y + dy, z + dz
            if 0 <= nx < H and 0 <= ny < N and 0 <= nz < M and box[nx][ny][nz] == 0:
                box[nx][ny][nz] = box[x][y][z] + 1
                tomato.append((nx, ny, nz))
    
    ret = float("-inf")
    for height in box:
        for row in height:
            if 0 in row:
                return -1
            ret = max(ret, max(row))
    return ret - 1

print(bfs())


# 날짜(레벨)별로 탐색하기.
# 메모리: 58300KB / 시간: 1492ms
from sys import stdin


input = stdin.readline
M, N, H = map(int, input().split())  # M: 열, N: 행, H: 높이
box = [[list(map(int, input().split())) for _ in range(N)] for _ in range(H)]
curr = []

for i in range(H):
    for j in range(N):
        for k in range(M):
            if box[i][j][k] == 1:
                curr.append((i, j, k))

directions = [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]

def bfs():
    global curr
    
    count = -1
    while curr:
        nxt = []
        for x, y, z in curr:
            for dx, dy, dz in directions:
                nx, ny, nz = x + dx, y + dy, z + dz
                if 0 <= nx < H and 0 <= ny < N and 0 <= nz < M and box[nx][ny][nz] == 0:
                    box[nx][ny][nz] = 1
                    nxt.append((nx, ny, nz))
        count += 1
        curr = nxt
        
    for height in box:
        for row in height:
            if 0 in row:
                return -1
    return count

print(bfs())