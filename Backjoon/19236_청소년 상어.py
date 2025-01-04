# 문제집 - 0x0D강 - 시뮬레이션


# 문제: https://www.acmicpc.net/problem/19236
# 메모리: 32412KB / 시간: 40ms
from sys import stdin


input = stdin.readline

field = []
fish = {}  # 물고기 번호: (물고기 좌표)

# 방향 벡터
dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, -1, -1, -1, 0, 1, 1, 1]

for i in range(4):
    line = list(map(int, input().split()))
    new_line = []
    for j in range(0, 7, 2):
        new_line.append((line[j], line[j+1]-1))
        fish[line[j]] = (i, j//2)
    field.append(new_line)

# (0, 0) 물고기부터 먹고 시작
shark_loc = (0, 0)
max_num, shark_dir = field[0][0]
field[0][0] = (0, 0)
del fish[max_num]


# 물고기 이동 함수
def fish_moving(field, fish, shark_loc: tuple):
    for i in range(1, 17):
        if i not in fish:  # 이미 먹힌 물고기라면 pass
            continue

        x, y = fish[i]
        d = field[x][y][1]
        flag = True

        while flag:
            nx, ny = x + dx[d], y + dy[d]

            if 0 <= nx < 4 and 0 <= ny < 4 and shark_loc != (nx, ny):
                break

            d = (d + 1) % 8
            if d == field[x][y][1]:  # 360º 돌아서 원래 방향이 될 때까지 이동가능한 좌표가 없다면 포기
                flag = False
        
        if not flag:
            continue

        if field[nx][ny] != (0, 0):  # 이동하려는 좌표에 다른 물고기가 있다면
            prev_fish = field[nx][ny][0]
            fish[prev_fish] = (x, y)

        field[x][y] = (i, d)
        field[x][y], field[nx][ny] = field[nx][ny], field[x][y]
        fish[i] = (nx, ny)


# 상어 이동 함수
def shark_moving(field, fish, shark_loc, shark_dir, S: int):
    global max_num

    # 기존 필드 복제 후 fish_moving 실행
    field = [line[:] for line in field]  # tuple을 immutable 객체이므로 깊은 복사 필요 X
    fish = fish.copy()

    fish_moving(field, fish, shark_loc)

    x, y = shark_loc
    d = shark_dir

    while True:
        x += dx[d]
        y += dy[d]

        if x < 0 or x >= 4 or y < 0 or y >= 4:  # 필드를 벗어나면 최대값 업데이트 후 break
            max_num = max(S, max_num)
            break
        
        if field[x][y] == (0, 0):  # 빈 공간이라면 해당 좌표는 건너뜀
            continue
        
        f_num, f_dir = field[x][y]
        field[x][y] = (0, 0)
        del fish[f_num]

        shark_moving(field, fish, (x, y), f_dir, S + f_num)
        # DFS 실행 후 복원
        fish[f_num] = (x, y)
        field[x][y] = (f_num, f_dir)


shark_moving(field, fish, (0, 0), shark_dir, max_num)
print(max_num)