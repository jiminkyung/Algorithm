# 문제집 - 0x0D강 - 시뮬레이션


# 문제: https://www.acmicpc.net/problem/21608
# 메모리: 31120KB / 시간: 160ms
from sys import stdin


input = stdin.readline

N = int(input())
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
room = [[0] * N for _ in range(N)]
empty = [[0] * N for _ in range(N)]
student = {}

# 키: 값 = 번호: [좋아하는 학생들]
for _ in range(N * N):
    line = list(map(int, input().split()))
    student[line[0]] = line[1:]

# 꼭짓점은 2로, 가장자리는 3으로, 그 외에는 4로 빈칸 수 저장
for i in range(N):
    for j in range(N):
        if 0 < i < N-1 and 0 < j < N-1:
            empty[i][j] = 4
        else:
            empty[i][j] = 3
empty[0][0] = empty[0][N-1] = empty[N-1][0] = empty[N-1][N-1] = 2


def checking(number):
    candidates = []

    for i in range(N):
        for j in range(N):
            if room[i][j] == 0:
                like_cnt = empty_cnt = 0

                for dx, dy in directions:
                    nx, ny = i + dx, j + dy
                    if 0 <= nx < N and 0 <= ny < N:
                        if room[nx][ny] in student[number]:
                            like_cnt += 1
                        elif room[nx][ny] == 0:
                            empty_cnt += 1
                
                # 후보 리스트에 (좋아하는 학생 수, 빈칸 수, 행, 열) 저장
                candidates.append((like_cnt, empty_cnt, i, j))
    
    # 좋아하는 학생이 많을수록, 빈칸이 많을수록, 행/열이 작을수록
    candidates.sort(key=lambda x: (-x[0], -x[1], x[2], x[3]))
    return candidates[0][2], candidates[0][3]


for key in student:
    x, y = checking(key)
    room[x][y] = key
    # 자리를 결정했다면 해당 자리 주위로 빈칸 수를 하나씩 줄여줌
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if 0 <= nx < N and 0 <= ny < N:
            empty[nx][ny] -= 1

satisfaction = 0

for i in range(N):
    for j in range(N):
        number = room[i][j]
        cnt = 0

        for dx, dy in directions:
            nx, ny = i + dx, j + dy
            if 0 <= nx < N and 0 <= ny < N:
                if room[nx][ny] in student[number]:
                    cnt += 1
        if cnt != 0:
            satisfaction += 10 ** (cnt - 1)

print(satisfaction)