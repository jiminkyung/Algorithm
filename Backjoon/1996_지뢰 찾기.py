# 구현


# 문제: https://www.acmicpc.net/problem/1996
# 메모리: 88400KB / 시간: 1256ms
from sys import stdin


input = stdin.readline

def main():
    N = int(input())
    
    def check(N):
        data = [input().rstrip() for _ in range(N)]
        field = [["0"] * N for _ in range(N)]

        # 방향: 동서남북 + 대각선
        dx = [-1, -1, 0, 1, 1, 1, 0, -1]
        dy = [0, 1, 1, 1, 0, -1, -1, -1]

        for i in range(N):
            for j in range(N):
                # 지뢰면 표시 후 넘어감
                if data[i][j] != ".":
                    field[i][j] = "*"
                    continue

                # 지뢰 수 체크
                bomb = 0

                for d in range(8):
                    nx = i + dx[d]
                    ny = j + dy[d]

                    # 체크할 좌표가 범위 내에 존재하고, 땅이 아니라면 카운트
                    if not (0 <= nx < N and 0 <= ny < N):
                        continue
                    
                    if data[nx][ny] != ".":
                        bomb += int(data[nx][ny])
                
                field[i][j] = str(bomb) if bomb < 10 else "M"
        
        return field
    

    field = check(N)

    for line in field:
        print("".join(line))


main()


# 3x3 크기를 미리 구하고 계산하는 코드!
# y: 현재 행. 현재 행 기준으로 -1, +1 행을 솎아낸다 -> zip으로 각 열의 합을 구함
# 출처👉 https://www.acmicpc.net/source/97413943
import sys

input = lambda: sys.stdin.readline().rstrip()

N = int(input())
mine = [[int(c) if c.isdigit() else 0 for c in input()] for _ in range(N)]

for y in range(N):
    line = []
    arr = list(map(sum, zip(*mine[max(0, y - 1) : y + 2])))
    for x in range(N):
        if mine[y][x]:
            line.append("*")
        else:
            count = sum(arr[max(0, x - 1) : x + 2])
            count_str = str(count) if count < 10 else "M"
            line.append(count_str)
    print("".join(line))