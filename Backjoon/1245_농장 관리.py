# 너비 우선 탐색 (BFS)


# 문제: https://www.acmicpc.net/problem/1245

# 같은 높이를 가진 좌표들을 탐색 + 방문처리
# 탐색 중 더 높은 좌표가 주변에 존재한다면, 현재 탐색중인 높이는 봉우리가 될 수 없음.
# 만약 주변에 더 높은 좌표가 없다면, 현재 높이가 봉우리인 셈.

"""
반례 데이터👉 https://www.acmicpc.net/board/view/142917

8 7
4 3 2 2 1 0 1
3 3 3 2 1 0 1
2 2 2 2 1 0 0
2 1 1 1 1 0 0
1 1 6 6 0 1 0
0 0 0 1 1 1 0
0 1 2 2 5 1 0
0 1 1 1 2 1 0
"""

# 메모리: 32412KB / 시간: 48ms
from sys import stdin


input = stdin.readline

def main():
    N, M = map(int, input().split())
    field = [list(map(int, input().split())) for _ in range(N)]
    visited = [[False] * M for _ in range(N)]

    def bfs(x, y, height) -> bool:
        # 대각선까지 체크
        dx = [1, 0, -1, 0, 1, -1, 1, -1]
        dy = [0, 1, 0, -1, 1, -1, -1, 1]

        curr = [(x, y)]
        visited[x][y] = True
        # 현재 봉우리 주위로 더 높은 봉우리가 있다면, 현재 봉우리는 산봉우리 X
        is_top = True

        while curr:
            nxt = []
            for x, y in curr:
                for i in range(8):
                    nx, ny = x + dx[i], y + dy[i]
                    if not (0 <= nx < N and 0 <= ny < M):
                        continue
                    if field[nx][ny] > height:
                        is_top = False
                    if not visited[nx][ny] and field[nx][ny] == height:
                        visited[nx][ny] = True
                        nxt.append((nx, ny))
            curr = nxt
        return is_top
    

    cnt = 0

    for i in range(N):
        for j in range(M):
            if not visited[i][j] and field[i][j] != 0:
                cnt += bfs(i, j, field[i][j])

    print(cnt)


main()