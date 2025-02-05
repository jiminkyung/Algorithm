# 문제집 - 0x0D강 - 시뮬레이션


# 문제: https://www.acmicpc.net/workbook/view/7316

# 🚨 무지개블록은 모든 그룹에 중복으로 포함될 수 있다! 정확히 명세되어있지 않음.
# 메모리: 35156KB / 시간: 88ms
from sys import stdin
from collections import deque


input = stdin.readline

N, M = map(int, input().split())

field = [list(map(int, input().split())) for _ in range(N)]
score = 0  # 획득한 점수


def bfs(field: list, visited: list, x: int, y: int):
    queue = deque([(x, y)])
    visited[x][y] = True
    rainbow = []  # 무지개 블록
    color = field[x][y]  # 현재 블록의 색
    cnt = 1  # 전체 블록의 갯수
    b = (x, y)  # 기준 블록

    while queue:
        x, y = queue.popleft()

        for nx, ny in ((x-1, y), (x+1, y), (x, y-1), (x, y+1)):
            if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny]:
                if field[nx][ny] == color or field[nx][ny] == 0:
                    if field[nx][ny] == 0:  # 무지개 블록일경우 rainbow에 추가
                        rainbow.append((nx, ny))
                    elif field[nx][ny] == color:  # 일반 블록일경우 기준 블록 업데이트
                        b = min(b, (nx, ny))
                    visited[nx][ny] = True
                    queue.append((nx, ny))
                    cnt += 1
    
    if cnt >= 2:  # 총 블록이 2개 이상이라면 그룹 리스트에 추가
        blocks.append((cnt, len(rainbow), *b))
        for rx, ry in rainbow:  # 무지개 블록들은 여러 그룹에 중복으로 속할 수 있으므로 방문 취소
            visited[rx][ry] = False


# 선택한 블록 그룹 제거 함수
def delete(field: list, x, y):
    visited = [[False] * N for _ in range(N)]
    visited[x][y] = True
    color = field[x][y]
    queue = deque([(x, y)])
    field[x][y] = -2  # 없앤 블록은 -2로 설정

    while queue:
        x, y = queue.popleft()

        for nx, ny in ((x-1, y), (x+1, y), (x, y-1), (x, y+1)):
            if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny]:
                if field[nx][ny] == color or field[nx][ny] == 0:  # 일반 블록 or 무지개 블록일경우 -2 처리
                    visited[nx][ny] = True
                    field[nx][ny] = -2
                    queue.append((nx, ny))


# 중력 가동 함수
def gravity(field: list):
    for col in range(N):
        # 열 고정. 행을 아래에서부터 위로 순회.
        for row in range(N-1, -1, -1):
            if field[row][col] == -2:
                curr = row - 1  # 현재 위치로 이동시킬 블록의 행
                while curr >= 0:
                    # 검은 블록은 통과할 수 없으므로 멈춤
                    if field[curr][col] == -1:
                        break

                    # 일반 블록 or 무지개 블록이라면 현재 블록으로 끌어당김
                    if field[curr][col] != -2:
                        field[row][col] = field[curr][col]
                        field[curr][col] = -2
                        break

                    curr -= 1


# 배열을 반시계방향으로 90º 회전시키는 함수
def rotate(field):
    return [[field[j][N-1-i] for j in range(N)] for i in range(N)]


# 블록 그룹이 없을때까지 게임 진행
while True:
    # 1. 블록 그룹들을 저장
    visited = [[False] * N for _ in range(N)]
    blocks = []

    for i in range(N):
        for j in range(N):
            if not visited[i][j] and field[i][j] > 0:
                bfs(field, visited, i, j)
    
    if not blocks:  # 그룹이 없다면 게임 종료
        break

    # 2. 제거할 블록 그룹 선별, 점수 업데이트
    blocks.sort(key=lambda x: (-x[0], -x[1], -x[2], -x[3]))  # 블록의 수, 무지개 블록의 수, 행, 열 기준 내림차순 정렬
    new_score, _, target_x, target_y = blocks[0]
    score += new_score ** 2  # 획득한 점수 업데이트
    
    # 3. 그룹 삭제, 중력 가동, 회전
    delete(field, target_x, target_y)
    gravity(field)
    field = rotate(field)
    gravity(field)


print(score)