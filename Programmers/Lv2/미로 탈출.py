# 문제: https://school.programmers.co.kr/learn/courses/30/lessons/159993

# BFS로 풀이. 방문체크 시 레버 사용 정보가 필요함.
# 똑같은 좌표 (x, y)를 방문해도, 레버를 사용했을때와 안 했을때의 (x, y)는 다른 좌표임.
# -> visited를 3차원 배열로 관리.
from collections import deque


def solution(maps: list[str]):
    N, M = len(maps), len(maps[0])
    # visited[x][y][l]: 레버의 상태가 l이었을때 (x, y)좌표에 방문한 적 있는지.
    visited = [[[False] * 2 for _ in range(M)] for _ in range(N)]
    
    # start 위치 찾기
    x = y = -1
    flag = False
    
    for i in range(N):
        for j in range(M):
            if maps[i][j] == "S":
                x, y = i, j
                flag = True
                break
        if flag:
            break
    
    # x, y, 레버유무, 카운트
    queue = deque([(x, y, 0, 0)])
    visited[x][y][0] = True
    
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    
    ret = -1
    
    while queue:
        x, y, l, cnt = queue.popleft()
        
        # 현재 위치가 출구이고, 레버를 당긴 상태라면 값 저장 후 break
        if maps[x][y] == "E" and l:
            ret = cnt
            break
        
        # 현재 위치가 레버칸이라면 당기고 visited 갱신
        if maps[x][y] == "L":
            l = 1
            visited[x][y][l] = True
        
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            
            if not (0 <= nx < N and 0 <= ny < M) or maps[nx][ny] == "X":
                continue
                
            if not visited[nx][ny][l]:
                visited[nx][ny][l] = True
                queue.append((nx, ny, l, cnt + 1))
        
    return ret