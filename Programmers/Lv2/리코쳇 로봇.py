# 문제: https://school.programmers.co.kr/learn/courses/30/lessons/169199

# 처음엔 방향값까지 포함해서 3차원 배열로 visited를 관리했으나...
# 이렇게되면 장애물 없이 이동하는 중간에도 다른 방향으로 전환 가능.
# -> 현 위치에서 동서남북으로 쭉 미끄러진 다음, 해당 위치를 큐에 추가하는 방식으로 변경.
from collections import deque


def solution(board: list[str]):
    N, M = len(board), len(board[0])

    # 초기 위치 찾기
    x = y = -1
    found = False

    for i in range(N):
        for j in range(M):
            if board[i][j] == "R":
                x, y = i, j
                found = True
                break
        
        if found:
            break
    
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    
    queue = deque([(x, y, 0)])
    visited = [[False] * M for _ in range(N)]

    while queue:
        x, y, cnt = queue.popleft()
        cx, cy = x, y

        # 골인지점이면 바로 반환. (어차피 뒤에는 벽 or 장애물)
        if board[x][y] == "G":
            return cnt
        
        # 동서남북으로 미끄러지기.
        for i in range(4):
            cx, cy = x, y
            while True:
                nx, ny = cx + dx[i], cy + dy[i]

                # 벽 or 장애물을 만날때까지 반복
                if not (0 <= nx < N and 0 <= ny < M) or board[nx][ny] == "D":
                    break

                cx, cy = nx, ny
            
            if not visited[cx][cy]:
                visited[cx][cy] = True
                queue.append((cx, cy, cnt + 1))
                
    return -1