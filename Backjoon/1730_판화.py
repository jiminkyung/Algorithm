# 구현
# 시뮬레이션


# 문제: https://www.acmicpc.net/problem/1730
# 메모리: 32412KB / 시간: 32ms
from sys import stdin


input = stdin.readline

def main():
    N = int(input())
    directions = {"D": (1, 0), "U": (-1, 0), "L": (0, -1), "R": (0, 1)}
    # -1: 방문X, 0: - 방문, 1: ㅣ 방문, 2: + 방문
    visited = [[-1] * N for _ in range(N)]
    x = y = 0

    for d in input().rstrip():
        dx, dy = directions[d]
        nx, ny = x + dx, y + dy

        # 격자를 벗어난다면 좌표 처리 X
        if nx < 0 or nx >= N or ny < 0 or ny >= N:
            continue

        if d == "D" or d == "U":
            # 이동 전 좌표 처리
            if visited[x][y] == -1:
                visited[x][y] = 1
            elif visited[x][y] == 0:
                visited[x][y] = 2
            # 이동 후
            if visited[nx][ny] == -1:
                visited[nx][ny] = 1
            elif visited[nx][ny] == 0:
                visited[nx][ny] = 2
        else:  # 좌우이동
            # 이동 전 좌표 처리
            if visited[x][y] == -1:
                visited[x][y] = 0
            elif visited[x][y] == 1:
                visited[x][y] = 2
            # 이동 후
            if visited[nx][ny] == -1:
                visited[nx][ny] = 0
            elif visited[nx][ny] == 1:
                visited[nx][ny] = 2
        
        x, y = nx, ny
    
    path = {-1: ".", 0: "-", 1: "|", 2: "+"}
    for line in visited:
        print("".join(map(lambda x: path[x], line)))


main()