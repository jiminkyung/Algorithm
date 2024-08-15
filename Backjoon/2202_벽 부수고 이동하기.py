# 그래프와 순회

# 3차원 리스트로 visited를 만든다. [x][y][벽 안부숨, 벽 부숨] 형태다.


# 가장 흔한 방식.
# 메모리: 188980KB / 시간: 3820ms
from sys import stdin
from collections import deque


input = stdin.readline
N, M = map(int, input().split())
MAP = [list(map(int, input().rstrip())) for _ in range(N)]

directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
queue = deque([(0, 0, 0)])
visited = [[[0, 0] for _ in range(M)] for _ in range(N)]

visited[0][0][0] = 1

def bfs():
    while queue:
        x, y, cnt = queue.popleft()

        if (x, y) == (N-1, M-1):
            return visited[x][y][cnt]

        for dir_x, dir_y in directions:
            nx, ny = x + dir_x, y + dir_y
            if 0 <= nx < N and 0 <= ny < M:
                if MAP[nx][ny] == 1 and cnt == 0:
                    visited[nx][ny][1] = visited[x][y][0] + 1
                    queue.append((nx, ny, 1))
                elif MAP[nx][ny] == 0 and visited[nx][ny][cnt] == 0:
                    visited[nx][ny][cnt] = visited[x][y][cnt] + 1
                    queue.append((nx, ny, cnt))
    return -1

print(bfs())


# 스택으로 큐 없이 풀이.
# 메모리: 161176KB / 시간: 2936ms
from sys import stdin


input = stdin.readline
N, M = map(int, input().split())
MAP = [list(map(int, input().rstrip())) for _ in range(N)]

directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

def bfs():
    visited = [[[0, 0] for _ in range(M)] for _ in range(N)]
    visited[0][0][0] = 1
    curr = [(0, 0, 0)]
    
    count = 1
    while curr:
        nxt = []
        for x, y, brk in curr:
            if x == N-1 and y == M-1:
                return count
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < N and 0 <= ny < M:
                    if MAP[nx][ny] == 1 and brk == 0:
                        visited[nx][ny][1] = 1
                        nxt.append((nx, ny, 1))
                    elif MAP[nx][ny] == 0 and visited[nx][ny][brk] == 0:
                        visited[nx][ny][brk] = 1
                        nxt.append((nx, ny, brk))
        curr = nxt
        count += 1
    return -1

print(bfs())


# 👑 가장 효율이 좋은 코드
# [벽 안부숨, 벽 부숨]을 boolean값으로 설정하고, 거리를 나타낼 dis를 따로 할당해주기.
# 메모리: 151288KB / 시간: 2660ms
from sys import stdin
from collections import deque


input = stdin.readline
N, M = map(int, input().split())
MAP = [list(map(int, input().rstrip())) for _ in range(N)]

def bfs():
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    queue = deque([(0, 0, 1, False)])  # x, y, distance, 벽을 부쉈는지 여부
    visited = [[[False, False] for _ in range(M)] for _ in range(N)]  # [벽 안부숨, 벽 부숨]
    visited[0][0][False] = True

    while queue:
        x, y, dis, broken = queue.popleft()

        if x == N-1 and y == M-1:
            return dis
        
        for dx, dy in directions:
            nx, ny = x + dx, y + dy

            if 0 <= nx < N and 0 <= ny < M:
                # 벽이 아닌 경우,
                if MAP[nx][ny] == 0 and not visited[nx][ny][broken]:
                    visited[nx][ny][broken] = True
                    queue.append((nx, ny, dis+1, broken))
                # 벽인 경우, 아직 벽을 부수지 않았다면,
                # 여기서 방문체크를 꼭 해주지 않아도 되지만, 효율성을 위해 적는게 좋다.
                # '다른 경로를 통해 벽을 부순 경우'도 고려하는것. 👉 마찬가지로 위의 두 코드도 방문체크코드를 추가해주면 더 빨라진다.
                elif MAP[nx][ny] == 1 and not broken and not visited[nx][ny][True]:
                    visited[nx][ny][True] = True
                    queue.append((nx, ny, dis+1, True))

    return -1  # 목적지에 도달할 수 없는 경우

print(bfs())