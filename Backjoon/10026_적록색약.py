# 문제집 - 대학생 기본반


# 문제: https://www.acmicpc.net/problem/10026
# 메모리: 31120KB / 시간: 44ms
from sys import stdin


input = stdin.readline

def bfs(sx, sy, color):
    curr = [(sx, sy)]
    visited[sx][sy] = True
    
    while curr:
        nxt = []
        for x, y in curr:
            for nx, ny in ((x-1, y), (x, y-1), (x+1, y), (x, y+1)):
                if 0 <= nx < N and 0 <= ny < N:
                    if not visited[nx][ny] and grid[nx][ny] == color:
                        visited[nx][ny] = True
                        nxt.append((nx, ny))
        curr = nxt
    return 1

N = int(input())

grid = [input().rstrip() for _ in range(N)]
ret1 = ret2 = 0

# 적록색약이 아닌 사람
visited = [[False] * N for _ in range(N)]
for i in range(N):
    for j in range(N):
        if not visited[i][j]:
            ret1 += bfs(i, j, grid[i][j])

# 적록색약인 사람
visited = [[False] * N for _ in range(N)]
grid = [row.replace("R", "G") for row in grid]

for i in range(N):
    for j in range(N):
        if not visited[i][j]:
            ret2 += bfs(i, j, grid[i][j])

print(ret1, ret2)