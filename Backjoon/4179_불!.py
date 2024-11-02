# 문제집 - 0x09강 - BFS


# 문제: https://www.acmicpc.net/problem/4179
# 참고👉 https://seongonion.tistory.com/87

"""
두개의 큐를 사용해야하는 문제다.
큐1은 불이 번지는 경로를, 큐2는 지훈이의 경로를 담는다.

visited 역시 각각 하나씩 생성해야한다.
각 visited[x][y]에는 걸리는 시간값이 들어간다.

주어진 입력값을 임시변수 line에 할당한뒤, 해당 line의 열을 탐색한다.
F, J, # 일때로 ,나눴는데 F, J일때에는 각 큐에 (i, j)값을 넣어준 후 visited[i][j]를 1로 설정한다.
=> bfs()함수는 별다른 인자값 없이 실행되므로 미리 설정해두는게 훨씬 수월하다.
그리고 line을 maze 리스트에 추가한다.

bfs()함수 실행은 다음과 같다.
먼저 불의 경로를 visited_f에 저장한다음 지훈이의 경로를 탐색한다.
새로운 경로를 nx, ny 라고 할 때, 범위를 벗어나는지부터 체크한다.
만약 범위를 벗어났다면 탈출에 성공했다는 뜻이므로 visited_j[x][y]값을 반환해준다.
=> 왜냐하면 J는 벽, 불을 제외한 곳에 위치해있고 범위를 벗어나기 전까진 유효경로 내에 존재함.
아니라면 visited_f[nx][ny]의 값, 즉 (nx, ny)위치에 불이 도달하는 시간보다 (x, y)+1 이 더 작은지 체크한다.
지훈이가 (nx, ny)에 도달하는 시간이 더 짧을경우 visited_j[nx][ny]의 값을 업데이트 해주고 큐에 위치 추가.
"""
# 메모리: 64776KB / 시간: 1376ms
from sys import stdin
from collections import deque


input = stdin.readline

R, C = map(int, input().split())
directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
maze = []

queue_j = deque([])
queue_f = deque([])

visited_j = [[0] * C for _ in range(R)]
visited_f = [[0] * C for _ in range(R)]

for i in range(R):
    line = input().rstrip()

    for j in range(C):
        if line[j] == "J":
            queue_j.append((i, j))
            visited_j[i][j] = 1
        elif line[j] == "F":
            queue_f.append((i, j))
            visited_f[i][j] = 1
        elif line[j] == "#":
            visited_f[i][j] = 1
            visited_j[i][j] = 1
    maze.append(line)

def bfs():
    while queue_f:
        x, y = queue_f.popleft()

        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < R and 0 <= ny < C:
                if visited_f[nx][ny] == 0:
                    visited_f[nx][ny] = visited_f[x][y] + 1
                    queue_f.append((nx, ny))
    
    while queue_j:
        x, y = queue_j.popleft()

        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < R and 0 <= ny < C:
                if visited_j[nx][ny] != 0:
                    continue
                if visited_f[nx][ny] == 0 or visited_f[nx][ny] > visited_j[x][y] + 1:
                    visited_j[nx][ny] = visited_j[x][y] + 1
                    queue_j.append((nx, ny))
            else:
                return visited_j[x][y]
                
    return "IMPOSSIBLE"

print(bfs())