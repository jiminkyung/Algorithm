# 그래프 이론
# 그래프 탐색
# 너비 우선 탐색
# 깊이 우선 탐색
# 격자 그래프
# 플러드 필


# 문제: https://www.acmicpc.net/problem/4963
# 메모리: 33432KB / 시간: 52ms
from sys import stdin


input = stdin.readline

def main():
    while True:
        w, h = map(int, input().split())

        if (w, h) == (0, 0):
            break

        print(check(w, h))


def check(C, R) -> int:
    field = [list(map(int, input().split())) for _ in range(R)]
    
    def dfs(x, y):
        dx = [1, 0, -1, 0, 1, 1, -1, -1]
        dy = [0, 1, 0, -1, 1, -1, 1, -1]

        stack = [(x, y)]

        while stack:
            x, y = stack.pop()

            if field[x][y] != 1:
                continue
            field[x][y] = -1

            for i in range(8):
                nx, ny = x + dx[i], y + dy[i]

                # (nx, ny)가 땅인 경우에만 스택에 추가
                if not (0 <= nx < R and 0 <= ny < C) or field[nx][ny] != 1:
                    continue

                stack.append((nx, ny))


    cnt = 0

    # (i, j)가 땅일 경우 탐색
    for i in range(R):
        for j in range(C):
            if field[i][j] == 1:
                dfs(i, j)
                cnt += 1
    
    return cnt


main()