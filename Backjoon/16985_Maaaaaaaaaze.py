# 문제집 - 0x0D강 - 시뮬레이션


# 문제: https://www.acmicpc.net/problem/16985
# 15683_감시, 18809_Gaaaaaaaaaarden 와 비슷한 문제.

# 1. bfs()내에서 ret 업데이트 (더 깔끔)
# 메모리: 34176KB / 시간: 952ms
from sys import stdin
from collections import deque


input = stdin.readline

maze =[[list(map(int, input().split())) for _ in range(5)] for _ in range(5)]
cube = [[[0] * 5 for _ in range(5)] for _ in range(5)]
dx = [1, -1, 0, 0, 0, 0]
dy = [0, 0, 1, -1, 0, 0]
dz = [0, 0, 0, 0, 1, -1]
ret = int(1e9)

def bfs(cube):
    global ret

    visited = [[[0] * 5 for _ in range(5)] for _ in range(5)]
    queue = deque([(0, 0, 0)])

    while queue:
        x, y, z = queue.popleft()

        if (x, y, z) == (4, 4, 4):
            # 나올수있는 최솟값이 12이므로, 결과값이 12라면 출력 후 실행 종료.
            if visited[4][4][4] == 12:
                print(12)
                exit()
            ret = min(ret, visited[4][4][4])
            return

        for i in range(6):
            nx = x + dx[i]
            ny = y + dy[i]
            nz = z + dz[i]

            if 0 <= nx < 5 and 0 <= ny < 5 and 0 <= nz < 5:
                if visited[nx][ny][nz] != 0 or cube[nx][ny][nz] == 0:
                    continue
                visited[nx][ny][nz] = visited[x][y][z] + 1
                queue.append((nx, ny, nz))

# 90º씩 회전시키는 함수
def rotate(floor):
    rotated = [[0] * 5 for _ in range(5)]

    for i in range(5):
        for j in range(5):
            rotated[j][4-i] = floor[i][j]
    return rotated

# 각 판의 회전각도에 따라 bfs()를 실행시키는 함수
def dfs(n):
    if n == 5:
        # 출구로 나올 수 있는 경우에만 bfs()실행
        if cube[4][4][4] == 1:
            bfs(cube)
        return
    
    for _ in range(4):
        # 해당각도에서 입구로 출입 가능하다면 각도 고정 후 다음 판으로 넘어감.
        if cube[0][0][0] == 1:
            dfs(n+1)
        cube[n] = rotate(cube[n])  # 모든 각도로 돌려보기


used = [False] * 5
def ordering(per):
    # 5개의 판을 모두 사용했다면 생성된 순열에 담긴 번호대로 cube에 저장
    if len(per) == 5:
        for i in range(5):
            cube[i] = maze[per[i]]
        dfs(0)
        return
    
    for i in range(5):
        if used[i]:
            continue
        per.append(i)
        used[i] = True
        ordering(per)
        used[i] = False
        per.pop()


ordering([])
print(ret if ret != int(1e9) else -1)


# 2. dfs()내에서 ret 업데이트
# 메모리: 34176KB / 시간: 952ms
from sys import stdin
from collections import deque


input = stdin.readline

maze =[[list(map(int, input().split())) for _ in range(5)] for _ in range(5)]
cube = [[[0] * 5 for _ in range(5)] for _ in range(5)]
dx = [1, -1, 0, 0, 0, 0]
dy = [0, 0, 1, -1, 0, 0]
dz = [0, 0, 0, 0, 1, -1]
ret = int(1e9)

def bfs(cube):
    visited = [[[0] * 5 for _ in range(5)] for _ in range(5)]
    queue = deque([(0, 0, 0)])

    while queue:
        x, y, z = queue.popleft()

        if (x, y, z) == (4, 4, 4):
            return visited[4][4][4]

        for i in range(6):
            nx = x + dx[i]
            ny = y + dy[i]
            nz = z + dz[i]

            if 0 <= nx < 5 and 0 <= ny < 5 and 0 <= nz < 5:
                if visited[nx][ny][nz] != 0 or cube[nx][ny][nz] == 0:
                    continue
                visited[nx][ny][nz] = visited[x][y][z] + 1
                queue.append((nx, ny, nz))
    return

def rotate(floor):
    rotated = [[0] * 5 for _ in range(5)]

    for i in range(5):
        for j in range(5):
            rotated[j][4-i] = floor[i][j]
    return rotated

def dfs(n):
    global ret

    if n == 5:
        if cube[4][4][4] == 1:
            bfs_ret = bfs(cube)
            if bfs_ret == 12:
                print(12)
                exit()  
            if bfs_ret:
                ret = min(ret, bfs_ret)
        return
    
    for _ in range(4):
        if cube[0][0][0] == 1:
            dfs(n+1)
        cube[n] = rotate(cube[n])

used = [False] * 5
def ordering(per):
    if len(per) == 5:
        for i in range(5):
            cube[i] = maze[per[i]]
        dfs(0)
        return
    
    for i in range(5):
        if used[i]:
            continue
        per.append(i)
        used[i] = True
        ordering(per)
        used[i] = False
        per.pop()

ordering([])
print(ret if ret != int(1e9) else -1)