# 문제집 - 0x0D강 - 시뮬레이션


# 문제: https://www.acmicpc.net/problem/21610
# 메모리: 31120KB / 시간: 200ms
from sys import stdin


input = stdin.readline

N, M = map(int, input().split())

# ←, ↖, ↑, ↗, →, ↘, ↓, ↙
dx = [0, -1, -1, -1, 0, 1, 1, 1]
dy = [-1, -1, 0, 1, 1, 1, 0, -1]
# 대각선 체크
diagonal = [(-1, -1), (-1, 1), (1, -1), (1, 1)]

field = [list(map(int, input().split())) for _ in range(N)]
clouds = [(N-1, 0), (N-1, 1), (N-2, 0), (N-2, 1)]


def moving(d, s, clouds: list):
    used = set()
    s %= N

    # 구름 이동 후 해당지역에 물 1 추가
    for x, y in clouds:
        nx, ny = x + dx[d] * s, y + dy[d] * s

        # 좌표 인덱스 조정
        if nx < 0:
            nx = N + nx
        elif nx >= N:
            nx %= N
        
        if ny < 0:
            ny = N + ny
        elif ny >= N:
            ny %= N
        
        field[nx][ny] += 1
        used.add((nx, ny))

    # 대각선 체크 후 해당되는만큼 더해주기
    field_copy = [line[:] for line in field]
    for x, y in used:
        water_cnt = 0
        for r, c in diagonal:
            nx, ny = x + r, y + c
            if 0 <= nx < N and 0 <= ny < N and field[nx][ny] != 0:
                water_cnt += 1
        field_copy[x][y] += water_cnt
    return field_copy, used


def new_cloud(used: set) -> list:
    clouds = []

    for i in range(N):
        for j in range(N):
            if field[i][j] >= 2 and (i, j) not in used:
                clouds.append((i, j))
                field[i][j] -= 2
    return clouds


for k in range(M):
    d, s = map(int, input().split())
    field, used = moving(d-1, s, clouds)
    clouds = new_cloud(used)

water = sum(sum(line) for line in field)
print(water)