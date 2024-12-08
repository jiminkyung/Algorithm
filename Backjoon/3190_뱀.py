# 문제집 - 0x0D강 - 시뮬레이션


# 문제: https://www.acmicpc.net/problem/3190
# 메모리: 34088KB / 시간: 56ms
from sys import stdin
from collections import deque


input = stdin.readline

N = int(input())
board = [[0] * N for _ in range(N)]

K = int(input())
for _ in range(K):
    x, y = map(int, input().split())
    board[x-1][y-1] = 2

L = int(input())
directions = deque()
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

for _ in range(L):
    X, C = input().rstrip().split()
    directions.append((int(X), C))

snake = deque([(0, 0)])
board[0][0] = 1
time = d = 0

while snake:
    time += 1
    x, y = snake[-1]  # 뱀의 머리 부분

    nx, ny = x + dx[d], y + dy[d]

    if not (0 <= nx < N and 0 <= ny < N) or board[nx][ny] == 1:
        break

    # 사과가 없다면 꼬리를 한 칸 땡김
    if board[nx][ny] == 0:
        tail_x, tail_y = snake.popleft()
        board[tail_x][tail_y] = 0
    board[nx][ny] = 1
    snake.append((nx, ny))

    if directions and directions[0][0] == time:
        _, new_d = directions.popleft()
        if new_d == "L":
            d = (d - 1) % 4  # 반시계로 90º
        else:
            d = (d + 1) % 4  # 시계로 90º

print(time)