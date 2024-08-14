# 그래프와 순회

# 첫번째 코드... 메모리 초과. 였지만 visited로 한번 방문했던 곳은 방문하지 못하게 처리 -> 통과.
# => 생각해보니 당연함. 좌표 x에서 갈 수 있는 6가지 경우, 그 각각의 경우에서 또 6가지의 경우... 이렇게 좌표 x에서 파생된 모든 경우를 이미 알고 있기 때문에.
# 메모리: 34200KB / 시간: 56ms

from sys import stdin
from collections import deque


input = stdin.readline
board = list(range(101))

N, M = map(int, input().split())

for _ in range(N):
    x, y = map(int, input().split())
    board[x] = y

for _ in range(M):
    x, y = map(int, input().split())
    board[x] = y

def bfs():
    visited = [False] * 101
    visited[0] = visited[1] = True
    queue = deque([(1, 0)])

    while queue:
        x, dis = queue.popleft()
        if x == 100:
            return dis
        for i in range(1, 7):
            nx = board[x] + i
            if 0 < nx <= 100 and not visited[nx]:
                visited[nx] = True
                queue.append((nx, dis+1))

print(bfs())