# 문제: https://school.programmers.co.kr/learn/courses/30/lessons/250136


# 효율성 테스트에서 살짝 걸렸던 문제.

# 첫번째 시도: 각 bfs마다 visited set 생성. 방문한 좌표들을 모두 저장.
# visited를 순회하며 열 체크. curr_col list에 석유 덩어리 값 저장.
# 마지막으로 col 0~M을 순회하며 curr_col 값을 col에 더해주기...
# -> 푸는게 목적이었던터라 더러웠음. visited, curr_col 제거 후 수정하니 통과.
from collections import deque


def solution(land: list[list]) -> int:
    N, M = len(land), len(land[0])
    col = [0] * M

    def bfs(x, y):
        nonlocal col, land

        queue = deque([(x, y)])
        land[x][y] = 0
        curr_col = [y]  # 현재 석유 덩어리에 포함되는 열들

        dx = [1, 0, -1, 0]
        dy = [0, 1, 0, -1]

        while queue:
            x, y = queue.popleft()

            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]

                if not (0 <= nx < N and 0 <= ny < M) or land[nx][ny] == 0:
                    continue

                land[nx][ny] = 0
                queue.append((nx, ny))
                curr_col.append(ny)
            
        cnt = len(curr_col)

        # 해당 열에 석유 덩어리 크기 더해주기.
        for y in set(curr_col):
            col[y] += cnt
    
    
    for x in range(N):
        for y in range(M):
            if land[x][y] == 1:
                bfs(x, y)
    
    return max(col)