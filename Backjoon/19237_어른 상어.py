# 문제집 - 0x0D강 - 시뮬레이션


# 문제: https://www.acmicpc.net/problem/19237
# 메모리: 32412KB / 시간: 180ms
from sys import stdin


input = stdin.readline

N, M, k = map(int, input().split())
directions = {1: (-1, 0), 2: (1, 0), 3: (0, -1), 4: (0, 1)}

shark_dir = {}
shark_pos = {}
field = []

for i in range(N):
    line = list(map(int, input().split()))
    for j in range(N):
        if line[j]:
            shark_pos[line[j]] = (i, j)
            line[j] = (line[j], k)
    field.append(line)

shark_curr_dir = {i+1: int(d) for i, d in enumerate(input().rstrip().split())}

for num in range(1, M+1):
    shark_dir[num] = {}
    for dir in range(1, 5):
        shark_dir[num][dir] = tuple(map(int, input().split()))

time = 0

def moving(field):
    new_field = [line[:] for line in field]
    new_shark_pos = {}

    # 1. 냄새 감소시키기
    for i in range(N):
        for j in range(N):
            if field[i][j]:
                shark, smell = field[i][j]
                if smell > 1:
                    new_field[i][j] = (shark, smell-1)
                else:
                    new_field[i][j] = 0
    
    # 2. 상어 이동시키기
    for shark in shark_pos:
        x, y = shark_pos[shark]
        curr_dir = shark_curr_dir[shark]
        found = False

        # 2-1. 빈칸 우선으로 이동
        for dir in shark_dir[shark][curr_dir]:
            nx, ny = x + directions[dir][0], y + directions[dir][1]

            if 0 <= nx < N and 0 <= ny < N and field[nx][ny] == 0:
                found = True

                if new_field[nx][ny] != 0:
                    prev_shark, _ = new_field[nx][ny]
                    if shark > prev_shark:
                        break
                    del new_shark_pos[prev_shark]
                        
                new_field[nx][ny] = (shark, k)
                new_shark_pos[shark] = (nx, ny)
                shark_curr_dir[shark] = dir
                break

        # 2-2. 본인 냄새 우선으로 이동
        if not found:
            for dir in shark_dir[shark][curr_dir]:
                nx, ny = x + directions[dir][0], y + directions[dir][1]
                
                if 0 <= nx < N and 0 <= ny < N and field[nx][ny] != 0:
                    if field[nx][ny][0] == shark:
                        new_field[nx][ny] = (shark, k)
                        new_shark_pos[shark] = (nx, ny)
                        shark_curr_dir[shark] = dir
                        break

    return new_field, new_shark_pos


# 🚨 1000초 "이상"이 되도 여러마리가 남아있다면 -1 출력
while time < 1000:
    field, shark_pos = moving(field)
    time += 1

    if len(shark_pos) == 1:  # 상어가 한마리만 남은 경우 break
        break
else:
    time = -1

print(time)