# 문제집 - 0x09강 - BFS


# 문제: https://www.acmicpc.net/problem/14442
# 1600_말이 되고픈 원숭이 문제와 매우 비슷하다. 조건부분만 적절히 수정하면 된다.

# PyPy3로 통과
# 메모리: 475756KB / 시간: 5408ms
from sys import stdin
from collections import deque


input = stdin.readline

def bfs():
    queue = deque([(0, 0, K)])
    # visited 초기화 시 0으로 설정하는것보다 -1로 설정하는것이 더 빠르다. 메모리는 0으로 설정하는편이 더 효율적이다.
    # 메모리부분은 이해하겠는데, 시간 측면에서 -1로 초기화하는편이 더 빠른 이유를 모르겠다...
    visited = [[[-1] * (K+1) for _ in range(M)] for _ in range(N)]
    visited[0][0][K] = 1
    
    while queue:
        x, y, k = queue.popleft()

        if x == N-1 and y == M-1:
            return visited[x][y][k]
        
        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y

            if 0 <= nx < N and 0 <= ny < M:
                if k > 0:
                    if graph[nx][ny] == 1 and visited[nx][ny][k-1] == -1:
                        visited[nx][ny][k-1] = visited[x][y][k] + 1
                        queue.append((nx, ny, k-1))
                if graph[nx][ny] == 0 and visited[nx][ny][k] == -1:
                    visited[nx][ny][k] = visited[x][y][k] + 1
                    queue.append((nx, ny, k))
    return -1

N, M, K = map(int, input().split())
graph = [list(map(int, input().rstrip())) for _ in range(N)]
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

print(bfs())


"""
리스트 생성 시, lst[3][100]이 lst[100][3]보다 효율적이다.
행 우선 방식을 사용하기 때문인데,
lst[3][100] 같은경우 lst[0][0]~lst[0][99]까지가 메모리에서 연속적인 위치에 저장된다.
반면 lst[100][3]은 lst[0][0]~lst[0][2]이 연속적으로 저장되는 형태다.

참고👉 https://www.acmicpc.net/board/view/111938
"""
# 메모리: 337472KB / 시간: 3400ms
from sys import stdin
from collections import deque


input = stdin.readline

def bfs():
    queue = deque([(K, 0, 0)])
    visited = [[[-1] * M for _ in range(N)] for _ in range(K+1)]
    visited[K][0][0] = 1
    
    while queue:
        k, x, y = queue.popleft()

        if x == N-1 and y == M-1:
            return visited[k][x][y]
        
        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y

            if 0 <= nx < N and 0 <= ny < M:
                if k > 0:
                    if graph[nx][ny] == 1 and visited[k-1][nx][ny] == -1:
                        visited[k-1][nx][ny] = visited[k][x][y] + 1
                        queue.append((k-1, nx, ny))
                if graph[nx][ny] == 0 and visited[k][nx][ny] == -1:
                    visited[k][nx][ny] = visited[k][x][y] + 1
                    queue.append((k, nx, ny))
    return -1

N, M, K = map(int, input().split())
graph = [list(map(int, input().rstrip())) for _ in range(N)]
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

print(bfs())


# 아래는 Python3로 통과된 풀이다.
# visited를 2차원 리스트로 작성하는 방식이다.
# visited[x][y]에는 벽을 깬 갯수가 담겨있다.
# 출처👉 https://www.acmicpc.net/source/83583155
""" Solution 2) 2D BFS """
def bfs():
    queue = deque([(0, 0, 1)])    
    delta = ((-1, 0), (1, 0), (0, -1), (0, 1))
    visited = [[11]*m for _ in range(n)]  # K의 범위는 0부터 10까지이므로 11로 초기화해준다.
    visited[0][0] = 0

    while queue:
        y, x, dist = queue.popleft()
        if y == n-1 and x == m-1: return dist
        
        for dy, dx in delta:
            ny, nx = y+dy, x+dx
            if 0<=ny<n and 0<=nx<m:
                b = visited[y][x] + grid[ny][nx]  # 지금까지 부순 벽의 갯수 + 벽 유무(0, 1)
                if b <= k and b < visited[ny][nx]:  # 부순 벽의 수(b)가 k이하고 기존 경로보다 적을때
                    visited[ny][nx] = b
                    queue.append((ny, nx, dist+1))

    return -1

n, m, k = map(int, input().split())
grid = [[*map(int, input().rstrip())] for _ in range(n)]
print(bfs())