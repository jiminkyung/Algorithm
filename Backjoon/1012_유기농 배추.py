# 그래프와 순회

# 메모리: 31120KB / 시간: 48ms
# DFS, BFS 선택 상관 없음. DFS 풀이.
# 주어진 1 좌표들로 탐색할까 생각해봤지만 더 비효율적일것같았다. 그냥 정석대로 풀이.

from sys import stdin


input = stdin.readline
T = int(input())
total = []

def dfs(x, y, m, n):
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    stack = [(x, y)]

    while stack:
        dx, dy = stack.pop()
        field[dx][dy] = 0
        for dir_x, dir_y in directions:
            nx, ny = dx + dir_x, dy + dir_y
            if nx >= m or nx < 0 or ny >= n or ny < 0:
                continue
            if field[nx][ny]:
                stack.append((nx, ny))
    return 1

for _ in range(T):
    M, N, K = map(int, input().split())
    field = [[0] * N for _ in range(M)]

    for _ in range(K):
        x, y = map(int, input().split())
        field[x][y] = 1
    
    count = 0
    for i in range(M):
        for j in range(N):
            if field[i][j]:
                count += dfs(i, j, M, N)

    total.append(count)

print(*total, sep="\n")