# 구현
# 브루트포스 알고리즘


# 문제: https://www.acmicpc.net/problem/3024
# 메모리: 32412KB / 시간: 36ms
from sys import stdin


input = stdin.readline

def main():
    N = int(input())

    def check(N: int, field: list[list]) -> str:
        # 오른쪽, 아래, 남동 대각선, 북동 대각선만 확인
        dx = [0, 1, 1, -1]
        dy = [1, 0, 1, 1]

        for x in range(N):
            for y in range(N):
                curr = field[x][y]

                if curr == ".":
                    continue

                # 알파벳이라면 네 방향 체크
                for i in range(4):
                    nx, ny = x + dx[i], y + dy[i]
                    nnx, nny = nx + dx[i], ny + dy[i]

                    # 해당 방향으로 두 칸으로 갔을때의 좌표 확인. 범위를 벗어나거나 알파벳이 다르면 pass
                    if not (0 <= nnx < N and 0 <= nny < N) or field[nnx][nny] != curr:
                        continue

                    # 해당 방향의 바로 앞 칸의 알파벳이 같다면 겜 끝. 현재칸, 현재+1칸, 현재+2칸 모두 같음.
                    if field[nx][ny] == curr:
                        return curr
        return "ongoing"
    

    field = [input().rstrip() for _ in range(N)]
    print(check(N, field))


main()