# 문제집 - 0x0D강 - 시뮬레이션


# 문제: https://www.acmicpc.net/problem/14499
# 문제에서 말하는 '윗면 1' => 우리가 바라보는 윗면이다. 주사위와 맞닿는 면은 6이다.

# 메모리: 31120KB / 시간: 40ms
from sys import stdin


input = stdin.readline

N, M, x, y, K = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]
# 인덱스 1부터 차례대로 동서남북을 가리킴
directions = [0, (0, 1), (0, -1), (-1, 0), (1, 0)]

# 0 + 주사위 6면. 주사위의 전개도대로 저장할 예정. 윗면은 1, 지도와 맞닿는 아랫면은 6이다.
dice = [0] * 7
commands = list(map(int, input().split()))


def rolling(direction):
    if direction == 1:  # 동
        dice[1], dice[4], dice[3], dice[6] = dice[4], dice[6], dice[1], dice[3]
    elif direction == 2:  # 서
        dice[1], dice[4], dice[3], dice[6] = dice[3], dice[1], dice[6], dice[4]
    elif direction == 3:  # 북
        dice[1], dice[2], dice[5], dice[6] = dice[5], dice[1], dice[6], dice[2]
    else:  # direction == 4, 남
        dice[1], dice[2], dice[5], dice[6] = dice[2], dice[6], dice[1], dice[5]


def checking(cx, cy, direction):
    dx, dy = directions[direction][0], directions[direction][1]
    nx, ny = cx + dx, cy + dy

    # 새 좌표값이 지도를 벗어나지 않는다면 굴림
    if 0 <= nx < N and 0 <= ny < M:
        rolling(direction)
        if graph[nx][ny] == 0:
            graph[nx][ny] = dice[6]
        else:
            dice[6] = graph[nx][ny]
            graph[nx][ny] = 0
        # 윗면 출력
        print(dice[1])
        return nx, ny
    # 지도를 벗어난다면 기존 좌표값 그대로 반환
    return cx, cy


for cmd in commands:
    x, y = checking(x, y, cmd)