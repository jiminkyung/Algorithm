# 문제집 - 0x0D강 - 시뮬레이션


# 문제: https://www.acmicpc.net/problem/16236
# 메모리: 32412KB / 시간: 120ms
from sys import stdin


input = stdin.readline

N = int(input())
field = []
shark = 2  # 상어의 크기
loc = 0  # 상어의 현재 위치

for i in range(N):
    line = list(map(int, input().split()))
    for j in range(N):
        if line[j] == 9:
            loc = (i, j)
            line[j] = 0
    field.append(line)


def bfs(x, y):
    curr = [(x, y, 0)]
    visited = [[False] * N for _ in range(N)]
    visited[x][y] = True
    fish = []

    while curr:
        nxt = []
        for x, y, dis in curr:
            for nx, ny in ((x-1, y), (x+1, y), (x, y-1), (x, y+1)):
                if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny]:
                    if field[nx][ny] <= shark:  # 칸이 0이거나 물고기의 사이즈가 shark 이하라면
                        visited[nx][ny] = True
                        nxt.append((nx, ny, dis+1))

                        if 0 < field[nx][ny] < shark:  # 먹을 수 있는 물고기라면 먹음
                            fish.append((dis+1, nx, ny))
        curr = nxt

    return fish


time = cnt = 0

while True:
    fish = bfs(*loc)

    if not fish:  # 더이상 먹을 수 있는 물고기가 없다면 break
        break

    fish.sort()
    dis, x, y = fish[0]

    loc = (x, y)
    field[x][y] = 0  # 물고기가 있던 칸을 0으로 바꿔줌
    time += dis
    cnt += 1

    if cnt == shark:
        shark += 1
        cnt = 0

print(time)