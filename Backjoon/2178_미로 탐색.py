# 그래프와 순회

# 최소한의 칸 수를 구하는 문제. BFS는 각 정점을 최단경로로 방문한다고 함.


# 첫번째 코드. 시간초과!
# => 큐에서 빼낸 후 방문체크(maze[x][y] = 0)를 함.
from sys import stdin
from collections import deque


input = stdin.readline
N, M = map(int, input().split())
maze = [list(map(int, input().rstrip())) for _ in range(N)]

def bfs():
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    queue = deque([(0, 0, 1)])

    while queue:
        x, y, dis = queue.popleft()
        maze[x][y] = 0

        if x == N-1 and y == M-1:
            return dis
        
        for dir_x, dir_y in directions:
            nx, ny = x + dir_x, y + dir_y

            if nx >= N or nx < 0 or ny >= M or ny < 0:
                continue
            if maze[nx][ny]:
                queue.append((nx, ny, dis+1))

print(bfs())


# 메모리: 34072KB / 시간: 68ms
# 🚨 BFS는 큐에 추가하기 전 방문 체크를 해야함.
from sys import stdin
from collections import deque


input = stdin.readline
N, M = map(int, input().split())
maze = [list(map(int, input().rstrip())) for _ in range(N)]

def bfs():
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    queue = deque([(0, 0, 1)])
    maze[0][0] = 0

    while queue:
        x, y, dis = queue.popleft()
        maze[x][y] = 0

        if x == N-1 and y == M-1:
            return dis
        
        for dir_x, dir_y in directions:
            nx, ny = x + dir_x, y + dir_y

            if nx >= N or nx < 0 or ny >= M or ny < 0:
                continue
            if maze[nx][ny]:
                maze[nx][ny] = 0
                queue.append((nx, ny, dis+1))

print(bfs())


# 큐 대신 스택 2개를 사용해서 풀 수도 있다. 36ms인 풀이코드.
# 현재 레벨에 해당하는 노드들을 저장하고 순회한다.
import sys
input = lambda : sys.stdin.readline().rstrip()
    
def bfs(a,b):
    curr = [[a,b]]

    count = 0
    while len(curr) > 0:
        to_visit = []  # 이전의 curr은 그대로 유지됨.
        for x in curr:
            i, j = x
            if i == n-1 and j == m-1: return count+1

            if maze[i][j] == '1':
                maze[i][j] = '0'

                if i > 0 and maze[i-1][j] == '1': to_visit.append([i-1,j])
                if j > 0 and maze[i][j-1] == '1': to_visit.append([i,j-1])
                if i < n-1 and maze[i+1][j] == '1': to_visit.append([i+1,j])
                if j < m-1 and maze[i][j+1] == '1': to_visit.append([i,j+1])

        curr = to_visit
        count += 1

n, m = map(int, input().split())
maze = [list(input()) for _ in range(n)]
print(bfs(0,0))