# 문제: https://school.programmers.co.kr/learn/courses/30/lessons/67259

# 처음엔 무작정 DFS -> 시간초과
# DP로 풀어도 될까?? 생각했지만 안됨. (x, y)의 최솟값이 아직 방문하지 않은 (x + i, y + j)의 값을 참고해야 할 수 있음.
# => 다익스트라, 또는 변형한 BFS로 풀이.
from heapq import heappush, heappop


def solution(board: list[list[int]]) -> int:
    N = len(board)
    INF = int(1e9)

    dx = [1, -1, 0, 0]
    dy = [0, 0, -1, 1]

    # dist[x][y][d]: (x, y) 좌표를 d 방향으로 방문했을때의 최소 비용 (d = 0: 상하, d = 1: 좌우)
    dist = [[[INF] * 2 for _ in range(N)] for _ in range(N)]

    heap = []

    # (0, 0) 다음으로 방문할 좌표들을 미리 처리.
    # 시작점 (0, 0)은 이전 이동 방향이 없으므로, 첫 번째 이동은 직선 도로 비용(100)으로만 추가.
    for i in range(4):
        nx = dx[i]
        ny = dy[i]

        if 0 <= nx < N and 0 <= ny < N and board[nx][ny] == 0:
            d = i // 2
            dist[nx][ny][d] = 100
            heappush(heap, (100, nx, ny, d))
    
    while heap:
        cost, x, y, d = heappop(heap)

        if cost > dist[x][y][d]:
            continue

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if not (0 <= nx < N and 0 <= ny < N) or board[nx][ny]:
                continue

            new_d = i // 2

            if new_d == d:
                new_cost = cost + 100
            else:
                new_cost = cost + 600
            
            if new_cost < dist[nx][ny][new_d]:
                dist[nx][ny][new_d] = new_cost
                heappush(heap, (new_cost, nx, ny, new_d))
    

    return min(dist[N-1][N-1])