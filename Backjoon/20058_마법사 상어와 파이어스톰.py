# 문제집 - 0x0D강 - 시뮬레이션


# 문제: https://www.acmicpc.net/problem/20058
# 메모리: 32412KB / 시간: 2812ms
from sys import stdin


input = stdin.readline

N, Q = map(int, input().split())
N = 2 ** N
field = [tuple(map(int, input().split())) for _ in range(N)]
L = list(map(int, input().split()))

# 각 블록을 90º 회전시키는 함수
def rotate(field, size: int) -> list:
    rotated = [[0] * N for _ in range(N)]
    # 딱 두번의 for문만으로도 풀 수 있을것같다... 더 구해봐야겠음.
    for i in range(0, N, size):
        for j in range(0, N, size):

            for row in range(i, i+size):
                for col in range(j, j+size):
                    rotated[col-j+i][(i+size)-(row-j)-1] = field[row][col]
    return rotated


# 인접한 얼음 수를 체크 후 녹이는 함수
def melt(field):
    melted = [line[:] for line in field]
    for x in range(N):
        for y in range(N):
            cnt = 0
            for nx, ny in ((x-1, y), (x+1, y), (x, y-1), (x, y+1)):
                if 0 <= nx < N and 0 <= ny < N and field[nx][ny]:
                    cnt += 1
            if cnt < 3:
                melted[x][y] = max(0, melted[x][y]-1)
    return melted


# 덩어리, 얼음의 합을 구하는 함수
def bfs(x, y):
    global total_ice

    curr = [(x, y)]
    visited[x][y] = True
    total_ice += field[x][y]
    chunk = 1

    while curr:
        nxt = []
        for x, y in curr:
            for nx, ny in ((x-1, y), (x+1, y), (x, y-1), (x, y+1)):
                if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny] and field[nx][ny]:
                    visited[nx][ny] = True
                    nxt.append((nx, ny))
                    chunk += 1
                    total_ice += field[nx][ny]
        curr = nxt
    return chunk


for size in L:
    size = 2 ** size
    field = rotate(field, size)
    field = melt(field)

visited = [[False] * N for _ in range(N)]
total_ice = max_chunk = 0

for i in range(N):
    for j in range(N):
        if not visited[i][j] and field[i][j]:
            max_chunk = max(bfs(i, j), max_chunk)

print(total_ice, max_chunk, sep="\n")