# 문제집 - 0x0D강 - 시뮬레이션


# 문제: https://www.acmicpc.net/problem/11559

"""
1. 처음에 작성했던 풀이 방식
- 필드 저장 시 문자열을 정수형으로 변환 (R: 1, G: 2...)
- 필드를 시계방향으로 90º 회전
- 뿌요 폭발 후 필드를 업데이트할때 수정 X, 새로운 배열 생성

=> 수월히 통과했으나 메모리, 실행시간이 다른 풀이들보다 살짝 높았다. 34140KB / 52ms
=> 알고보니 deque 모듈 때문이었음. 지우고 리스트만 사용하는 방식으로 bfs를 구현하니 31120KB / 32ms
"""

# 2. 조금 더 깔끔하게 수정한 풀이
# 필드를 뒤집는것은 동일하나, 터지는 뿌요들을 0으로 변환해준 뒤 필드 업데이트 진행.
# 만약 0이 아닌 뿌요가 나온다면 스택에 저장. 다음 행(변환전 열)으로 넘어갈때 스택 + [0] * 남은길이 로 현재 행 수정.
# 메모리: 31120KB / 시간: 32ms
from sys import stdin


input = stdin.readline

def bfs(x, y, color):
    curr = [(x, y)]
    visited[x][y] = True
    group = [(x, y)]

    while curr:
        nxt = []
        for x, y in curr:
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < 6 and 0 <= ny < 12 and not visited[nx][ny]:
                    if field[nx][ny] == color:
                        nxt.append((nx, ny))
                        group.append((nx, ny))
                        visited[nx][ny] = True
        curr = nxt
    return group


def bombing(): 
    for i in range(6):
        remain = []
        for j in range(12):
            if field[i][j] != 0:
                remain.append(field[i][j])
        field[i] = remain + [0] * (12 - len(remain))


directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
colors = {".": 0, "R": 1, "G": 2, "B": 3, "P": 4, "Y": 5}
field = [[0] * 12 for _ in range(6)]

for i in range(12):
    line = list(input().rstrip())
    for j in range(6):
        field[j][11-i] = colors[line[j]]

bomb = 0

while True:
    visited = [[False] * 12 for _ in range(6)]
    same = 0

    for i in range(6):
        for j in range(12):
            if field[i][j] != 0 and not visited[i][j]:
                puyo = bfs(i, j, field[i][j])
                if len(puyo) >= 4:
                    for x, y in puyo:
                        field[x][y] = 0
                    same += 1
    
    if same == 0:
        break

    bombing()
    bomb += 1

print(bomb)


# ⭐ 3. 다른 코드를 참고한 풀이.
# 이 방식이 제일 좋다. 열-행 순서로 순회하며 체크. 행 순회 시 11부터 거꾸로 순회.
# visited를 True/False가 아닌 정수형으로 초기화 후, 방문하지 않은 칸/방문한 칸/터뜨린 칸 을 다르게 표시.
# 열-행 순회 중 터뜨린 칸이 나오면 카운트, 터뜨리지 않은 칸이라면 [i+카운트][j] = [i][j]로 업데이트.
# 메모리: 31120KB / 시간: 32ms
from sys import stdin


input = stdin.readline

def bfs(x, y, color):
    curr = [(x, y)]
    visited[x][y] = 1
    group = [(x, y)]

    while curr:
        nxt = []
        for x, y in curr:
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < 12 and 0 <= ny < 6 and visited[nx][ny] == 0:
                    if field[nx][ny] == color:
                        nxt.append((nx, ny))
                        group.append((nx, ny))
                        visited[nx][ny] = 1
        curr = nxt
    return group


def update():
    for j in range(6):
        cnt = 0
        for i in range(11, -1, -1):
            if visited[i][j] == -1:
                cnt += 1
            else:
                if cnt > 0:
                    field[i+cnt][j] = field[i][j]
                    field[i][j] = 0


colors = {".": 0, "R": 1, "G": 2, "B": 3, "P": 4, "Y": 5}
field = []

for _ in range(12):
    line = list(input().rstrip())
    for i in range(6):
        line[i] = colors[line[i]]
    field.append(line)

directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
bomb = 0

while True:
    visited = [[False] * 6 for _ in range(12)]
    same = 0

    for i in range(12):
        for j in range(6):
            if field[i][j] != 0 and not visited[i][j]:
                group = bfs(i, j, field[i][j])

                if len(group) >= 4:
                    for x, y in group:
                        visited[x][y] = -1
                    same += 1
    
    if same == 0:
        break

    update()
    bomb += 1

print(bomb)