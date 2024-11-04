# 문제집 - 0x09강 - BFS


# 문제: https://www.acmicpc.net/problem/2468
# 메모리: 34088KB / 시간: 624ms
from sys import stdin
from collections import deque


input = stdin.readline

def bfs(height, x, y):
    queue = deque([(x, y)])
    visited[x][y] = True

    while queue:
        cx, cy = queue.popleft()

        for dx, dy in directions:
            nx, ny = cx + dx, cy + dy

            if 0 <= nx < N and 0 <= ny < N:
                if visited[nx][ny] == 0 and places[nx][ny] > height:
                    visited[nx][ny] = True
                    queue.append((nx, ny))
    return 1


N = int(input())

places = [list(map(int, input().split())) for _ in range(N)]
M = max(max(place) for place in places)
directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
ret = 0

for k in range(M):  # 범위를 0~가장큰수-1 로 잡아야함. 모든 땅의 높이가 1일경우, 비가 아예 안오는 경우(높이가 0)가 최댓값임.
    visited = [[False] * N for _ in range(N)]
    cnt = 0
    for i in range(N):
        for j in range(N):
            if places[i][j] > k and not visited[i][j]:
                cnt += bfs(k, i, j)
    ret = max(ret, cnt)

print(ret)