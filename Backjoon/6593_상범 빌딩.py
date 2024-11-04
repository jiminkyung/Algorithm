# 문제집 - 0x09강 - BFS


# 문제: https://www.acmicpc.net/problem/6593
# 메모리: 34104KB / 시간: 96ms
from sys import stdin
from collections import deque


input = stdin.readline

directions = [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]

def bfs():
    while queue:
        x, y, z = queue.popleft()

        if building[x][y][z] == "E":
            return f"Escaped in {visited[x][y][z] - 1} minute(s)."
        
        for dx, dy, dz in directions:
            nx, ny, nz = dx + x, dy + y, dz + z
            if 0 <= nx < L and 0 <= ny < R and 0 <= nz < C and visited[nx][ny][nz] == 0:
                visited[nx][ny][nz] = visited[x][y][z] + 1
                queue.append((nx, ny, nz))
    return "Trapped!"


while True:
    L, R, C = map(int, input().split())

    if L == 0 and R == 0 and C == 0:
        break

    building = []
    visited = [[[0] * C for _ in range(R)] for _ in range(L)]
    queue = deque([])

    for i in range(L):
        floor = []
        for j in range(R):
            line = input().rstrip()
            for k in range(C):
                if line[k] == "#":
                    visited[i][j][k] = 1
                elif line[k] == "S":
                    visited[i][j][k] = 1
                    queue.append((i, j, k))
            floor.append(line)
        input()
        building.append(floor)
    print(bfs())