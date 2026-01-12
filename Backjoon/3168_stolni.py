# 구현
# 해 구성하기
# 시뮬레이션


# 문제: https://www.acmicpc.net/problem/3168

# 구현 연습하기 좋은 문제. 크로아티아 문제 시리즈는 다 구현 연습하기 좋은듯??
# 메모리: 32412KB / 시간: 36ms
from sys import stdin


input = stdin.readline

def main():
    R, C = map(int, input().split())
    field = []
    pos = None

    for i in range(R):
        line = list(input().rstrip())
        field.append(line)
        for j in range(C):
            if line[j] == "L":
                pos = (i, j)
    
    field = solve(*pos, field, R, C)
    for line in field:
        print(*line, sep="")
    
    
def solve(x, y, field, R, C) -> list:
    dx = -1
    while y < C:
        nx, ny = x + dx, y + 1

        if ny == C:
            break

        # 공이 벽에 닿았다면 방향 전환
        if not (0 <= nx < R and 0 <= ny < C):
            dx *= -1
            continue

        # 공이 가야 할 자리에 선수가 있다면 이동시키기
        if field[nx][ny] == "|":
            field = move(nx, ny, field, R)

        field[nx][ny] = "L"
        x, y = nx, ny
    
    return field

def move(x, y, field, R) -> list:
    # 🚨 축구 보드게임처럼 한 열의 선수들은 세트로 움직여야함.

    # y열의 선수들 위치 저장 -> 일반 좌표로 변경
    player_pos = [i for i in range(R) if field[i][y] == "|"]
    for p in player_pos:
        field[p][y] = "."

    start = -player_pos[0]
    end = R - player_pos[-1] - 1

    # 선수 세트를 위 아래로 옮길 수 있는 범위
    for i in range(start, end+1):
        # i 크기만큼 옮겼을 때 공과 겹치지 않는다면 성공
        if all(p+i != x for p in player_pos):
            for p in player_pos:
                field[p+i][y] = "|"
            break

    return field


main()