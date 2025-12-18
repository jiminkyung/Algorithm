# 구현
# 브루트포스 알고리즘


# 문제: https://www.acmicpc.net/problem/3010
# 메모리: 32412KB / 시간: 32ms
from sys import stdin


input = stdin.readline

def main():
    # 애초에 앞뒤 모두 공백이 포함된 상태 그대로 주어짐.
    field = [input() for _ in range(7)]
    
    def check(field: list) -> int:
        cnt = 0

        dx = [0, 1, 0, -1]
        dy = [1, 0, -1, 0]

        for x in range(7):
            for y in range(7):
                # 현재 칸에 칩이 존재한다면 상하좌우 방향으로 체크.
                if field[x][y] == "o":
                    for i in range(4):
                        nx, ny = x + dx[i], y + dy[i]
                        nnx, nny = nx + dx[i], ny + dy[i]

                        if not (0 <= nx < 7 and 0 <= ny < 7) or not (0 <= nnx < 7 and 0 <= nny < 7):
                            continue

                        # 🗝️해당 방향으로 한 칸 앞에 칩, 그 다음칸은 빈칸일때 뛰어넘기 가능.
                        if field[nx][ny] == "o" and field[nnx][nny] == ".":
                            cnt += 1
        
        return cnt
    

    print(check(field))


main()