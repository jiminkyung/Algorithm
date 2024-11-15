# 문제집 - 0x0D강 - 시뮬레이션


# 문제: https://www.acmicpc.net/problem/18808

# 시간이 조금 더 빠른 코드.
# 메모리: 31252KB / 시간: 220ms
from sys import stdin


input = stdin.readline

# 실행할때마다 90도씩 회전
def rotate(sticker):
    R, C = len(sticker), len(sticker[0])
    rotated = [[0] * R for _ in range(C)]

    for i in range(R):
        for j in range(C):
            rotated[j][R-1-i] = sticker[i][j]
    return rotated

# 붙일 수 있는지 체크
def checking(sticker, R, C, x, y):
    if x + R > N or y + C > M:
        return False

    for i in range(R):
        for j in range(C):
            if sticker[i][j] == 1:
                if board[x+i][y+j] == 1:
                    return False
    return True

# 실제로 붙이기
def placing(sticker, R, C, x, y):
    for i in range(R):
        for j in range(C):
            if sticker[i][j] == 1:
                board[x+i][y+j] = 1

N, M, K = map(int, input().split())
board = [[0] * M for _ in range(N)]
stickers = []

for _ in range(K):
    R, C = map(int, input().split())
    sticker = [list(map(int, input().split())) for _ in range(R)]
    stickers.append(sticker)

for sticker in stickers:
    for _ in range(4):
        R, C = len(sticker), len(sticker[0])
        placed = False
        # 자연스럽게 좌측 상단, 우측 상단, 좌측 하단, 우측 하단의 순서로 진행됨
        for i in range(N):
            for j in range(M):
                if checking(sticker, R, C, i, j):
                    placing(sticker, R, C, i, j)
                    placed = True
                    break  # j 빠져나옴
            if placed:
                break  # i 빠져나옴
        if placed:
            break  # 방향 for문 빠져나옴
        sticker = rotate(sticker)

ret = sum(sum(line) for line in board)
print(ret)


# 메모리 효율이 조금 더 좋은 버전. checking, placing 함수에서 파라미터 R, C 제거
# 메모리: 31120KB / 시간: 228ms
from sys import stdin


input = stdin.readline

def rotate(sticker):
    R, C = len(sticker), len(sticker[0])
    rotated = [[0] * R for _ in range(C)]

    for i in range(R):
        for j in range(C):
            rotated[j][R-1-i] = sticker[i][j]
    return rotated

def checking(sticker, x, y):
    R, C = len(sticker), len(sticker[0])
    
    if x + R > N or y + C > M:
        return False

    for i in range(R):
        for j in range(C):
            if sticker[i][j] == 1:
                if board[x+i][y+j] == 1:
                    return False
    return True

def placing(sticker, x, y):
    R, C = len(sticker), len(sticker[0])
    
    for i in range(R):
        for j in range(C):
            if sticker[i][j] == 1:
                board[x+i][y+j] = 1

N, M, K = map(int, input().split())
board = [[0] * M for _ in range(N)]
stickers = []

for _ in range(K):
    R, C = map(int, input().split())
    sticker = [list(map(int, input().split())) for _ in range(R)]
    stickers.append(sticker)

for sticker in stickers:
    for _ in range(4):
        placed = False
        for i in range(N):
            for j in range(M):
                if checking(sticker, i, j):
                    placing(sticker, i, j)
                    placed = True
                    break  # j 빠져나옴
            if placed:
                break  # i 빠져나옴
        if placed:
            break  # 방향 for문 빠져나옴
        sticker = rotate(sticker)

ret = sum(sum(line) for line in board)
print(ret)