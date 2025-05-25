# 너비 우선 탐색 (BFS)


# 문제: https://www.acmicpc.net/problem/1303
# 메모리: 32412KB / 시간: 44ms
from sys import stdin


input = stdin.readline

def main():
    # 🚨 N-열, M-행 을 의미함.
    N, M = map(int, input().split())
    field = [input().rstrip() for _ in range(M)]

    B = W = 0
    visited = [[False] * N for _ in range(M)]

    def bfs(x, y, color):
        curr = [(x, y)]
        visited[x][y] = True
        cnt = 1

        dx = [1, 0, -1, 0]
        dy = [0, 1, 0, -1]

        while curr:
            nxt = []
            for x, y in curr:
                for i in range(4):
                    nx = x + dx[i]
                    ny = y + dy[i]
                    if not (0 <= nx < M and 0 <= ny < N):
                        continue
                    if field[nx][ny] == color and not visited[nx][ny]:
                        visited[nx][ny] = True
                        nxt.append((nx, ny))
                        cnt += 1
            curr = nxt
        
        return cnt ** 2


    for i in range(M):
        for j in range(N):
            if not visited[i][j]:
                if field[i][j] == "B":
                    B += bfs(i, j, "B")
                else:
                    W += bfs(i, j, "W")
    
    print(W, B)


main()