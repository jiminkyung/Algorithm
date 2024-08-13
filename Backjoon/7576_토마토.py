# 그래프와 순회

"""
1(익은 토마토)가 여러개 주어지므로, 박스를 순회하며 1을 발견할때마다 큐에 추가한다.
-> 출발점이 여러개인 BFS
이 초기의 큐를 가지고 BFS를 실행한다. 여러개의 익은 토마토가 동시에 미치는 영향을 계산할 수 있게된다.
-> 각 토마토 위치에서 탐색을 시작. 날짜가 지날때마다 count에 1을 추가한다.
-> 초기 날짜는 -1일로 설정한다. 처음 토마토의 상태는 0일이고, 모든 토마토가 다 익어도 +1이 실행되기 때문.
""" 


# 메모리: 145624KB / 시간: 1092ms
# 스택 2개로 풀이
from sys import stdin


input = stdin.readline
M, N = map(int, input().split())

box = [list(map(int, input().split())) for _ in range(N)]
directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
curr = []
count = -1

for i in range(N):
    for j in range(M):
        if box[i][j] == 1:
            curr.append((i, j))

def bfs():
    global count
    global curr

    while curr:
        nxt = []
        for x, y in curr:
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < N and 0 <= ny < M and box[nx][ny] == 0:
                    box[nx][ny] = 1
                    nxt.append((nx, ny))
        count += 1
        curr = nxt
    
    for row in box:
        if 0 in row:
            return -1

    return count

print(bfs())


# 큐로 풀이
# 메모리: 98532KB / 시간: 1072ms
from sys import stdin
from collections import deque


input = stdin.readline
M, N = map(int, input().split())

box = [list(map(int, input().split())) for _ in range(N)]
directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
tomato = deque([])

for i in range(N):
    for j in range(M):
        if box[i][j] == 1:
            tomato.append((i, j))

def bfs():
    while tomato:
        x, y = tomato.popleft()
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < M and box[nx][ny] == 0:
                box[nx][ny] = box[x][y] + 1
                tomato.append((nx, ny))
    
    ret = float("-inf")
    for row in box:
        if 0 in row:
            return -1
        ret = max(ret, max(row))
    return ret - 1

print(bfs())