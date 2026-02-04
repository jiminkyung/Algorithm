# 그래프 이론
# 그래프 탐색
# 너비 우선 탐색
# 깊이 우선 탐색
# 격자 그래프


# 문제: https://www.acmicpc.net/problem/3187

# 3184_양 문제와 똑같음. 양이 o가 아닌 k로 주어진다는점만 수정.
# 메모리: 34456KB / 시간: 84ms
from sys import stdin


input = stdin.readline

def main():
    R, C = map(int, input().split())

    field = [input().rstrip() for _ in range(R)]
    S = W = 0

    visited = [[False] * C for _ in range(R)]

    for i in range(R):
        for j in range(C):
            if not visited[i][j] and field[i][j] != "#":
                s, w, visited = dfs(field, R, C, i, j, visited)
                S += s
                W += w

    print(S, W)


def dfs(field, R, C, x, y, visited) -> tuple[int, int, list]:
    s = w = 0
    stack = [(x, y)]

    dx = [1, 0, -1, 0]
    dy = [0, -1, 0, 1]

    while stack:
        x, y = stack.pop()

        if visited[x][y]:
            continue

        # 늑대, 양 카운트
        if field[x][y] == "v":
            w += 1
        elif field[x][y] == "k":
            s += 1

        visited[x][y] = True

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            # 울타리일경우 pass
            if not (0 <= nx < R and 0 <= ny < C) or visited[nx][ny] or field[nx][ny] == "#":
                continue
            
            stack.append((nx, ny))
    
    # 개체 수 조절
    if s > w:
        w = 0
    else:
        s = 0
    return s, w, visited


main()