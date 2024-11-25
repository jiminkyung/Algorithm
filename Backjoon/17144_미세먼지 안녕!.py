# 문제집 - 0x0D강 - 시뮬레이션


# 문제: https://www.acmicpc.net/problem/17144

# 처음에 큐를 사용해서 풀었으나 장렬히 실패.
# 한번 퍼진 미세먼지도 양이 충분하다면 계속 퍼질 수 있고, '같은 시간에 한번에' 퍼져야하기 때문에 큐는 적절치 않음.
# 또한, 공기청정기는 항상 1열(A[x][0])에 위치함!!!

# 메모리: 31120KB / 시간: 1884ms
from sys import stdin


input = stdin.readline

R, C, T = map(int, input().split())
A = []

air_cleaner = []
directions = [(0, 1), (-1, 0), (0, -1), (1, 0)]

for i in range(R):
    line = list(map(int, input().split()))
    A.append(line)
    for j in range(C):
        if line[j] == -1:  # 항상 1열에 위치하기때문에 행만 저장
            air_cleaner.append(i)


def spread_dust():
    A_copy = [line[:] for line in A]

    for i in range(R):
        for j in range(C):
            if A[i][j] > 0:
                new_dust = A[i][j] // 5
                cnt = 0
                for dx, dy in directions:
                    nx, ny = i + dx, j + dy
                    if 0 <= nx < R and 0 <= ny < C and A[nx][ny] != -1:
                        A_copy[nx][ny] += new_dust
                        cnt += 1
                A_copy[i][j] -= new_dust * cnt
    return A_copy

# ⭐ 공기청정기에서 퍼져나가는 쪽이 빨아들이는 쪽부터 업데이트한다.

# 공기청정기의 윗부분
def cleaning_top():
    top = air_cleaner[0]

    # 위 -> 아래로 빨아들이기
    for i in range(top-1, 0, -1):
        A[i][0] = A[i-1][0]
    # 오른쪽 -> 왼쪽으로
    for i in range(C-1):
        A[0][i] = A[0][i+1]
    # 아래 -> 위
    for i in range(top):
        A[i][C-1] = A[i+1][C-1]
    # 왼쪽 -> 오른쪽
    for i in range(C-1, 1, -1):
        A[top][i] = A[top][i-1]
    A[top][1] = 0

# 공기청정기의 아랫부분
def cleaning_bottom():
    bottom = air_cleaner[1]

    # 아래 -> 위
    for i in range(bottom+1, R-1):
        A[i][0] = A[i+1][0]
    # 오른쪽 -> 왼쪽
    for i in range(C-1):
        A[R-1][i] = A[R-1][i+1]
    # 위 -> 아래
    for i in range(R-1, bottom, -1):
        A[i][C-1] = A[i-1][C-1]
    # 왼쪽 -> 오른쪽
    for i in range(C-1, 1, -1):
        A[bottom][i] = A[bottom][i-1]
    A[bottom][1] = 0


for _ in range(T):
    A = spread_dust()
    cleaning_top()
    cleaning_bottom()

ret = 0
for row in A:
    for col in row:
        if col > 0:
            ret += col

print(ret)