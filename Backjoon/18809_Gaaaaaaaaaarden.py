# 문제집 - 0x0C강 - 백트래킹


# 문제: https://www.acmicpc.net/problem/18809

# PyPy3로 통과한 코드.
# 메모리: 142476KB / 시간: 1652ms
from sys import stdin
from itertools import combinations
from collections import deque

input = stdin.readline

def bfs(green, red):
    visited = [[0] * M for _ in range(N)]
    queue = deque()
    flowers = 0

    for gx, gy in green:
        visited[gx][gy] = (1, 0)
        queue.append((gx, gy, 1, 0))
    for rx, ry in red:
        visited[rx][ry] = (-1, 0)
        queue.append((rx, ry, -1, 0))
    
    while queue:
        x, y, color, time = queue.popleft()

        if visited[x][y] == -1:  # 현재 좌표가 꽃이라면 continue
            continue

        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y

            if 0 <= nx < N and 0 <= ny < M and garden[nx][ny] != 0:
                if visited[nx][ny] == 0:  # 방문하지 않은 좌표라면 진행
                    visited[nx][ny] = (color, time+1)
                    queue.append((nx, ny, color, time+1))
                elif visited[nx][ny] == (-color, time+1):  # 다른 배양액이 뿌려진 좌표라면 꽃으로 업데이트
                    visited[nx][ny] = -1
                    flowers += 1
    return flowers


N, M, G, R = map(int, input().split())
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

garden = []
possible = []
max_flowers = 0

for i in range(N):
    line = list(map(int, input().split()))
    for j in range(M):
        if line[j] == 2:  # 배양액을 뿌릴 수 있는 좌표만 따로 저장
            possible.append((i, j))
    garden.append(line)

for comb in combinations(possible, G+R):
    for green_comb in combinations(comb, G):
        green = list(green_comb)  # 만들 수 있는 초록색 배양액 좌표
        red = [c for c in comb if c not in green]  # 빨간색 배양액 좌표
        max_flowers = max(bfs(green, red), max_flowers)

print(max_flowers)