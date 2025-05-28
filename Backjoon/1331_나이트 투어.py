# 구현
# 시뮬레이션


# 문제: https://www.acmicpc.net/problem/1331
# 메모리: 32412KB / 시간: 36ms
from sys import stdin


input = stdin.readline

def main():
    # 배열 기준 좌표값으로 변환시켜줌.
    # ex) A1 -> (0, 0)
    col = {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4, "F": 5}
    path = [input().rstrip() for _ in range(36)]

    visited = [[False] * 6 for _ in range(6)]
    # 출발지점 좌표
    start = path[0]
    x = 6 - int(start[1])
    y = col[start[0]]

    # 마지막 칸에서 출발지점으로 돌아올 수 있어야 하므로, 출발지점을 맨 뒤에 추가해서 모두 체크.
    for p in path[1:] + path[0:1]:
        nx = 6 - int(p[1])
        ny = col[p[0]]
        # 나이트는 L자로 이동해야함. 따라서 행렬 변화가 +(1, 2) 또는 +(2, 1) 이어야 됨.
        diff = abs(nx-x) + abs(ny-y)
        # 이동 조건에 맞지 않거나 이미 방문한 칸이라면 break
        if nx == x or ny == y or diff != 3 or visited[nx][ny]:
            print("Invalid")
            break
        
        visited[nx][ny] = True
        x, y = nx, ny
    else:
        print("Valid")


main()