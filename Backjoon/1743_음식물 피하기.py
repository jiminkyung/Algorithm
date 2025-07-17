# 그래프 이론
# 깊이 우선 탐색 (DFS)
# 너비 우선 탐색 (BFS)
# 플러드 필 => ?: 다차원 배열의 어떤 칸과 연결된 영역을 찾는 알고리즘


# 문제: https://www.acmicpc.net/problem/1743
# 메모리: 33432KB / 시간: 40ms
from sys import stdin


input = stdin.readline

def main():
    N, M, K = map(int, input().split())
    # 0: 빈칸, 1: 음식물있음, -1: 음식물있는지점 체크함
    field = [[0] * M for _ in range(N)]
    trash = []
    dx = [1, 0, -1, 0]
    dy = [0, -1, 0, 1]

    for _ in range(K):
        r, c = map(int, input().split())
        field[r-1][c-1] = 1
        trash.append((r-1, c-1))


    def bfs(x, y):
        curr = [(x, y)]
        field[x][y] = -1
        cnt = 1

        while curr:
            nxt = []
            for x, y in curr:
                for i in range(4):
                    nx = x + dx[i]
                    ny = y + dy[i]

                    if 0 > nx or nx >= N or 0 > ny or ny >= M:
                        continue
                    if field[nx][ny] == 1:
                        field[nx][ny] = -1
                        nxt.append((nx, ny))
                        cnt += 1
            curr = nxt
        return cnt
    

    max_trash = 0

    for r, c in trash:
        # 음식물이 있다면 bfs 실행. 실행 후 가장 큰 음식물 덩어리 갱신.
        if field[r][c] == 1:
            curr_trash = bfs(r, c)
            max_trash = max(max_trash, curr_trash)
    
    print(max_trash)


main()