# 문제집 - 0x0D강 - 시뮬레이션


# 문제: https://www.acmicpc.net/problem/23288
# 메모리: 32412KB / 시간: 44ms
from sys import stdin


input = stdin.readline

N, M, K = map(int, input().split())
field = [tuple(map(int, input().split())) for _ in range(N)]

# 주사위의 육면을 모두 기록.
# dice[x]: 전개도상에서 x면에 위치한 현재 숫자
# 🚨 초기 윗면 = 1, 바닥과 닿는 아랫면 = 6
dice = list(range(7))

# 동남서북 (시계방향)
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

# 초기 위치: (0, 0), 방향: 동
x = y = d = 0

# 칸별 점수 미리 계산해두기
score = [[0] * M for _ in range(N)]

def bfs(x, y, num):
    visited = set()
    visited.add((x, y))
    curr = [(x, y)]

    while curr:
        nxt = []
        for x, y in curr:
            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]
                if not (0 <= nx < N and 0 <= ny < M):
                    continue
                if (nx, ny) not in visited and field[nx][ny] == num:
                    nxt.append((nx, ny))
                    visited.add((nx, ny))
        curr = nxt
    
    point = num * len(visited)
    # 그룹에 포함된 좌표들에 점수 저장
    for x, y in visited:
        score[x][y] = point


for i in range(N):
    for j in range(M):
        if score[i][j] == 0:
            bfs(i, j, field[i][j])


def rolling(x, y, d) -> tuple[int, int, int]:
    nx, ny = x + dx[d], y + dy[d]

    # 이동할 칸이 범위 밖일경우 반대 방향으로
    if not (0 <= nx < N and 0 <= ny < M):
        d = (d + 2) % 4
        nx, ny = x + dx[d], y + dy[d]

    # 1. 동쪽
    if d == 0:
        dice[4], dice[6], dice[3], dice[1] = dice[6], dice[3], dice[1], dice[4]
    # 2. 남쪽
    elif d == 1:
        dice[2], dice[6], dice[5], dice[1] = dice[6], dice[5], dice[1], dice[2]
    # 3. 서쪽
    elif d == 2:
        dice[4], dice[6], dice[3], dice[1] = dice[1], dice[4], dice[6], dice[3]
    # 4. 북쪽
    else:
        dice[2], dice[6], dice[5], dice[1] = dice[1], dice[2], dice[6], dice[5]


    if dice[6] > field[nx][ny]:
        d = (d + 1) % 4
    elif dice[6] < field[nx][ny]:
        d = (d - 1) % 4
    
    return nx, ny, d


total_score = 0

for _ in range(K):
    x, y, d = rolling(x, y, d)
    total_score += score[x][y]

print(total_score)