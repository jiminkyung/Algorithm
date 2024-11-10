# 문제집 - 0x09강 - BFS


# 문제: https://www.acmicpc.net/problem/16933

# 낮/밤을 구분해야하므로 거리(칸)를 나타내는 변수 dis를 추가해줬다.
# (다음칸이 벽이지만 밤이라서 기다려야하는 경우) 처음에는 visited[x][y][k]에 1을 더해주는 방식을 사용했으나 틀림.
# => 상하좌우 4칸 중 2칸이 벽이라면, 첫번째 벽칸때문에 +1, 두번째 벽칸때문에 +1, 최종적으로 +2가 된다.
# => 쓰다보니 해결법이 생각났다. 아래에 추가 작성함.

# PyPy3로 통과된 코드. Python3로 통과된 풀이는 아직까진 없다.
# 메모리: 342312KB / 시간: 4412ms
from sys import stdin
from collections import deque


input = stdin.readline

def bfs():
    queue = deque([(K, 0, 0, 1)])
    visited = [[[-1] * M for _ in range(N)] for _ in range(K+1)]
    visited[K][0][0] = 1

    while queue:
        k, x, y, dis = queue.popleft()

        if x == N-1 and y == M-1:
            return dis

        for nx, ny in ((x-1, y), (x+1, y), (x, y-1), (x, y+1)):
            if 0 <= nx < N and 0 <= ny < M:
                if graph[nx][ny] == 0 and visited[k][nx][ny] == -1:
                    visited[k][nx][ny] = dis + 1
                    queue.append((k, nx, ny, dis+1))
                
                if k > 0:
                    # 다음칸이 벽일때
                    if graph[nx][ny] == 1 and visited[k-1][nx][ny] == -1:
                        if dis % 2 == 0:  # 밤
                            queue.append((k, x, y, dis+1))
                        else:  # 낮
                            visited[k-1][nx][ny] = dis + 1
                            queue.append((k-1, nx, ny, dis+1))

    return -1


N, M, K = map(int, input().split())
graph = [list(map(int, input().rstrip())) for _ in range(N)]

print(bfs())


# dis를 사용하지 않고 visited[k][x][y]로 낮/밤을 판별하는 풀이.
# 효율은 첫번째 풀이가 좋다.
# 메모리: 342816KB / 시간: 4464ms
from sys import stdin
from collections import deque


input = stdin.readline

def bfs():
    queue = deque([(K, 0, 0)])
    visited = [[[-1] * M for _ in range(N)] for _ in range(K+1)]
    visited[K][0][0] = 1

    while queue:
        k, x, y = queue.popleft()
        curr = visited[k][x][y]

        if x == N-1 and y == M-1:
            return curr

        for nx, ny in ((x-1, y), (x+1, y), (x, y-1), (x, y+1)):
            if 0 <= nx < N and 0 <= ny < M:
                if graph[nx][ny] == 0 and visited[k][nx][ny] == -1:
                    visited[k][nx][ny] = curr + 1
                    queue.append((k, nx, ny))
                
                if k > 0:
                    if graph[nx][ny] == 1 and visited[k-1][nx][ny] == -1:
                        if curr % 2 == 0:  # 밤
                            visited[k][x][y] = curr + 1
                            queue.append((k, x, y))
                        else:  # 낮
                            visited[k-1][nx][ny] = curr + 1
                            queue.append((k-1, nx, ny))

    return -1


N, M, K = map(int, input().split())
graph = [list(map(int, input().rstrip())) for _ in range(N)]

print(bfs())


# 아래는 Python3로 통과해보려 했으나 시간초과된 코드다.
from sys import stdin
from collections import deque


input = stdin.readline

def bfs():
    queue = deque([(0, 0, 1)])
    # visited[x][y] = (부순 벽의 수, 낮/밤 여부)
    visited = [[(float("inf"), -1)] * M for _ in range(N)]  
    visited[0][0] = (0, 1)  # 1은 낮, 0은 밤

    while queue:
        x, y, dis = queue.popleft()
        walls, is_day = visited[x][y]

        if x == N-1 and y == M-1:
            return dis

        for nx, ny in ((x-1, y), (x+1, y), (x, y-1), (x, y+1)):
            if 0 <= nx < N and 0 <= ny < M:
                next_walls = walls + graph[nx][ny]
                next_day = (dis + 1) % 2  # 다음이 낮(1)인지 밤(0)인지

                if next_walls <= K:
                    curr_walls, _ = visited[nx][ny]
                    
                    if graph[nx][ny] == 1:
                        if is_day:  # 현재가 낮
                            if next_walls < curr_walls:
                                visited[nx][ny] = (next_walls, next_day)
                                queue.append((nx, ny, dis+1))
                        else:  # 현재가 밤
                            queue.append((x, y, dis+1))  # 제자리에서 대기
                    else:  # 다음 칸이 길인 경우
                        if next_walls < curr_walls:  # 더 적은 벽을 부수고 도달 가능
                            visited[nx][ny] = (next_walls, next_day)
                            queue.append((nx, ny, dis+1))

    return -1

N, M, K = map(int, input().split())
graph = [list(map(int, input().rstrip())) for _ in range(N)]

print(bfs())