# 구현
# 브루트포스 알고리즘


# 문제: https://www.acmicpc.net/problem/3157

# 구현 연습하기 좋은 문제
# 메모리: 32412KB / 시간: 32ms
from sys import stdin


input = stdin.readline

def main():
    N = int(input())
    field = [list(input().rstrip()) for _ in range(N)]
    visited = [[False] * N for _ in range(N)]

    R = int(input())
    targets = [input().rstrip() for _ in range(R)]
    starts = {}

    # starts[x]: x로 시작하는 단어들
    for target in targets:
        starts.setdefault(target[0], []).append(target)

    for x in range(N):
        for y in range(N):
            # field[x][y]로 시작하는 문자가 있다면 체크
            if field[x][y] in starts:
                visited = check(field, visited, starts, x, y, N)
    
    ret = ""

    # 지워지지 않은 문자들 저장
    for i in range(N):
        for j in range(N):
            if not visited[i][j]:
                ret += field[i][j]
    
    print(ret)


def check(field: list, visited: list, starts: dict, x, y, N) -> list:
    dx = [0, 1, 0, -1, 1, 1, -1, -1]
    dy = [1, 0, -1, 0, -1, 1, -1, 1]

    for i in range(8):
        words = ""  # 현재 방향으로 모은 문자들
        pos = []    # 현재 방향으로 진행했을때의 좌표들
        for size in range(N):
            nx, ny = x + (dx[i] * size), y + (dy[i] * size)

            if not (0 <= nx < N and 0 <= ny < N):
                break

            pos.append((nx, ny))
            words += field[nx][ny]
        
        for target in starts[field[x][y]]:
            # field[x][y]로 시작하는 단어들 중 일치하는게 존재한다면, 방문처리(지워버리기)
            if target == words[:len(target)]:
                for j in range(len(target)):
                    visited[pos[j][0]][pos[j][1]] = True
    return visited


main()