# 문제집 - 0x0B - 재귀


# 문제: https://www.acmicpc.net/problem/2146

# 첫번째 시도는 시간초과, 두번째 시도부터는 틀렸다.
# 1) 섬마다 번호 부여, 경계선에 해당하는 좌표들은 edges에 저장
# 2) 각 섬의 경계선들을 하나하나 함수로 실행하며 최소값 체크
# => 2번이 문제였다. 하나씩 체크하는것이 아닌 한 섬의 모든 경계선 좌표들을 '한번에' 큐에 넣고 실행해야 올바른 답이 나온다.

# 메모리: 34156KB / 시간: 224ms
from sys import stdin
from collections import deque


input = stdin.readline

def bfs(x, y, num):
    queue = deque([(x, y)])
    visited[x][y] = num
    edge = []

    while queue:
        cx, cy = queue.popleft()
        is_edge = False

        for dx, dy in directions:
            nx, ny = dx + cx, dy + cy
            if 0 <= nx < N and 0 <= ny < N:
                if graph[nx][ny] == 0:
                    is_edge = True
                elif graph[nx][ny] == 1 and visited[nx][ny] == 0:
                    visited[nx][ny] = num
                    queue.append((nx, ny))
        if is_edge:
            edge.append((cx, cy))
    return edge

def making_bridge(edges, num):
    queue = deque()
    bridge = [[-1] * N for _ in range(N)]
    
    # 모든 가장자리를 시작점으로 추가
    for x, y in edges:
        queue.append((x, y))
        bridge[x][y] = 0

    while queue:
        cx, cy = queue.popleft()
        for dx, dy in directions:
            nx, ny = dx + cx, dy + cy
            if 0 <= nx < N and 0 <= ny < N:
                if graph[nx][ny] == 0 and bridge[nx][ny] == -1:
                    bridge[nx][ny] = bridge[cx][cy] + 1
                    queue.append((nx, ny))
                elif graph[nx][ny] == 1 and visited[nx][ny] != num:
                    return bridge[cx][cy]
    return float("inf")

N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]
directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
visited = [[0] * N for _ in range(N)]
edges = []
num = 1

# 섬 구분하고 가장자리 찾기
for i in range(N):
    for j in range(N):
        if graph[i][j] == 1 and visited[i][j] == 0:
            edges.append(bfs(i, j, num))
            num += 1

ret = float("inf")

# 각 섬에서 다른 섬까지의 최단 거리 찾기
num = 1
for edge in edges:
    ret = min(ret, making_bridge(edge, num))
    num += 1

print(ret)