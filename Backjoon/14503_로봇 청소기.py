# 문제집 - 0x0D강 - 시뮬레이션


# 문제: https://www.acmicpc.net/problem/14503
# 메모리: 31120KB / 시간: 44ms
from sys import stdin


input = stdin.readline

N, M = map(int, input().split())
r, c, d = map(int, input().split())
room = [list(map(int, input().split())) for _ in range(N)]

# 북, 동, 남, 서
directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]

def cleaning(x, y, d):
    cleaned = 0

    while True:
        # 현재 칸 청소여부 체크
        if room[x][y] == 0:
            cleaned += 1
            room[x][y] = -1

        for _ in range(4):
            # 반시계 방향으로 90도 회전
            d = (d + 3) % 4
            nx, ny = x + directions[d][0], y + directions[d][1]

            if 0 <= nx < N and 0 <= ny < M and room[nx][ny] == 0:
                x, y = nx, ny
                break
        # break에 걸리지 않으면(= 청소할곳이 없으면)
        else:
            nx, ny = x - directions[d][0], y - directions[d][1]
            if room[nx][ny] == 1:
                break
            # 후진 가능
            else:
                x, y = nx, ny
    return cleaned


print(cleaning(r, c, d))