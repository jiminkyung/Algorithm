# 문제집 - 0x0D강 - 시뮬레이션


# 문제: https://www.acmicpc.net/problem/14500
# 브루트포스로 분류되어 있지만 DFS를 사용해야 Python3로 통과할 수 있다.


# 1. PyPy3로 통과한 코드.
# 메모리: 119652KB / 시간: 3032ms
from sys import stdin


input = stdin.readline

N, M = map(int, input().split())
paper = [list(map(int, input().split())) for _ in range(N)]
# 순서대로 ㅡ ㅁ L ㄹ ㅜ
tetromino = [[[1, 1, 1, 1]], [[1, 1], [1, 1]], [[1, 0], [1, 0], [1, 1]],
             [[1, 0], [1, 1], [0, 1]], [[1, 1, 1], [0, 1, 0]]]

# 시계방향으로 90º 회전시키는 함수
def rotate(tetro):
    r, c = len(tetro), len(tetro[0])
    rotated = [[0] * r for _ in range(c)]

    for i in range(r):
        for j in range(c):
            rotated[j][r-1-i] = tetro[i][j]
    return rotated

# 좌우반전시키는 함수
def reverse(tetro):
    reversed = []

    for line in tetro:
        reversed.append(line[::-1])
    return reversed

# 해당 테트로미노를 붙일 수 있는지 체크하고, 붙일 수 있다면 계산
def checking(tetro, x, y):
    r, c = len(tetro), len(tetro[0])
    score = 0

    if x + r > N or y + c > M:
        return 0

    for i in range(r):
        for j in range(c):
            if tetro[i][j] == 1:
                score += paper[x+i][y+j]
    return score


max_score = 0

# (0, 0)부터 (N-1, N-1)까지 시도해보기
for idx, tetro in enumerate(tetromino):
    for i in range(N):
        for j in range(M):
            # 반전 유/무
            for _ in range(2):
                # 동서남북 회전시키기
                for _ in range(4):
                    max_score = max(checking(tetro, i, j), max_score)
                    # ㅁ 모양은 변화를 줘도 같으므로 패스
                    if idx == 1:
                        break
                    tetro = rotate(tetro)
                tetro = reverse(tetro)

print(max_score)


# ⭐ 2. Python3로 통과한 코드
# 참고👉 https://velog.io/@jajubal/%ED%8C%8C%EC%9D%B4%EC%8D%AC%EB%B0%B1%EC%A4%80-14500-%ED%85%8C%ED%8A%B8%EB%A1%9C%EB%AF%B8%EB%85%B8
# 메모리: 37996KB / 시간: 156ms
from sys import stdin


input = stdin.readline

def dfs(x, y, depth, total):
    """
    1. 선택한 경로의 현재까지의 점수(total) + (가장 높은 점수칸 * 앞으로의 칸)이
    현재까지의 최고 점수(max_score)보다 작다면 dfs 멈춤.
    => 앞으로 남은 칸을 모두 최고점으로 선택한다해도 max_score보다 낮기 때문에.

    2. 4칸 모두 선택했다면 최고 점수 비교 후 업데이트

    3. 현재 깊이가 1이라면 == 2칸 선택한 상태
    ㅗ 모양을 만들기 위해 (nx, ny)칸 선택 후 현재 칸(x, y)로 dfs 실행
    => ㄱ 모양까지 만든 후 꺾이는 부근에서 dfs를 실행하는 모양새
    """
    global max_score

    if max_score >= total + max_val * (3 - depth):
        return
    if depth == 3:
        max_score = max(total, max_score)
        return
    
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny]:
            if depth == 1:
                visited[nx][ny] = True
                dfs(x, y, depth + 1, total + paper[nx][ny])
                visited[nx][ny] = False
            visited[nx][ny] = True
            dfs(nx, ny, depth + 1, total + paper[nx][ny])
            visited[nx][ny] = False


N, M = map(int, input().split())
paper = [list(map(int, input().split())) for _ in range(N)]
visited = [[False] * M for _ in range(N)]
directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]

max_val = max(map(max, paper))  # peper에서 가장 높은 점수
max_score = 0

for i in range(N):
    for j in range(M):
        visited[i][j] = True
        dfs(i, j, 0, paper[i][j])
        visited[i][j] = False

print(max_score)