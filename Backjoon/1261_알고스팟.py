# 문제집 - 0x1D강 - 다익스트라 알고리즘


# 문제: https://www.acmicpc.net/problem/1261

# 2차원 다익스트라 문제
# 메모리: 35508KB / 시간: 52ms
from sys import stdin
from heapq import heappush, heappop


input = stdin.readline

M, N = map(int, input().split())
field = [list(map(int, list(input().rstrip()))) for _ in range(N)]
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

def dijkstra():
    heap = [(0, 0, 0)]  # (깬 벽의 수, x좌표, y좌표)
    walls = [[int(1e9)] * M for _ in range(N)]
    walls[0][0] = 0

    while heap:
        cnt, x, y = heappop(heap)

        if walls[x][y] < cnt:
            continue

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if not (0 <= nx < N and 0 <= ny < M):
                continue
            
            new_cnt = cnt + field[nx][ny]
            if new_cnt < walls[nx][ny]:
                walls[nx][ny] = new_cnt
                heappush(heap, (new_cnt, nx, ny))
    return walls[N-1][M-1]


print(dijkstra())