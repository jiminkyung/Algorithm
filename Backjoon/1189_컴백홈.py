# 백트래킹


# 문제: https://www.acmicpc.net/problem/1189
# 메모리: 32412KB / 시간: 128ms
from sys import stdin


input = stdin.readline

def main():
    R, C, K = map(int, input().split())
    field = [input().rstrip() for _ in range(R)]

    visited = [[False] * C for _ in range(R)]
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    cnt = 0

    def backtrack(x, y, dis, visited: list):
        nonlocal cnt

        # 만약 거리가 K일경우
        if dis == K:
            if (x, y) == (0, C-1):  # 좌표값이 도착점일경우 카운트 +1
                cnt += 1
            return
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < R and 0 <= ny < C and not visited[nx][ny]:
                if field[nx][ny] == ".":
                    visited[nx][ny] = True
                    backtrack(nx, ny, dis+1, visited)
                    visited[nx][ny] = False
    

    visited[R-1][0] = True
    backtrack(R-1, 0, 1, visited)  # 🚨 거리값 = 시작점과 도착점을 포함한 칸 수 이므로 1부터 시작한다.
    print(cnt)


main()