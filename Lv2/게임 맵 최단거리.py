# 클로드에게 배운 코드다. 난 못풀었다.

from collections import deque

def solution(maps):
    n, m = len(maps), len(maps[0])
    queue = deque([(0, 0, 1)])
    
    while queue:
        x, y, distance = queue.popleft()     
        if x == n - 1 and y == m - 1:
            return distance
        
        for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            nx, ny = x + dx, y + dy
            if nx < 0 or nx >= n or ny < 0 or ny >= m or maps[nx][ny] == 0:
                continue      
            if maps[nx][ny] == 1:
                maps[nx][ny] = 0 # 방문 처리
                queue.append((nx, ny, distance + 1)) # 큐에 추가
    return -1