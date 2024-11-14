# 문제집 - 0x0D강 - 시뮬레이션


# 문제: https://www.acmicpc.net/problem/15683
# 이건 참고 안하면 못풀겠다 헉ㅋㅋ
# 참고👉 https://velog.io/@ggb05224/%EB%B0%B1%EC%A4%80-15683-%EA%B0%90%EC%8B%9Cpython

# 메모리: 31120KB / 시간: 288ms
from sys import stdin


input = stdin.readline

N, M = map(int, input().split())

directions = {1: [[0], [1], [2], [3]],
              2: [[0, 2], [1, 3]],
              3: [[0, 1], [1, 2], [2, 3], [3, 0]],
              4: [[0, 1, 2], [1, 2, 3], [2, 3, 0], [3, 0, 1]],
              5: [[0, 1, 2, 3]]}
dx = [1, 0, -1, 0]  # 남, 동, 북, 서
dy = [0, 1, 0, -1]

office = []
empty = 0
cctv = []

for i in range(N):
    line = list(map(int, input().split()))
    for j in range(M):
        if 0 < line[j] < 6:
            cctv.append((line[j], i, j))
        elif line[j] == 0:
            empty += 1
    office.append(line)

def move(x, y, dir, office_copy):
    for d in dir:
        nx, ny = x, y

        while True:
            nx += dx[d]
            ny += dy[d]

            if not (0 <= nx < N and 0 <= ny < M) or office_copy[nx][ny] == 6:
                break
            if office_copy[nx][ny] != 0:
                continue
            office_copy[nx][ny] = "#"

def counting(office_copy):
    cnt = 0
    for line in office_copy:
        cnt += line.count(0)
    return cnt

def dfs(level, office):
    # 참고한 풀이에서는 copy 리스트를 두 번 생성해준다.
    # 나는 len(cctv)일경우 인자로 받은 리스트 그대로를 사용하고, for문 안에서만 copy리스트를 사용하도록 해줬다.
    # 시간은 368 -> 288로 100ms가량 단축됨.
    global empty
    if level == len(cctv):
        empty = min(counting(office), empty)
        return
    
    number, x, y = cctv[level]

    for dir in directions[number]:
        office_copy = [line[:] for line in office]
        move(x, y, dir, office_copy)
        dfs(level + 1, office_copy)

dfs(0, office)
print(empty)