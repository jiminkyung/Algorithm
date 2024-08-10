# 그래프와 순회

# DFS, BFS 중 아무거나 선택 가능. DFS로 풀이.
# 메모리: 31120KB / 시간: 40ms

from sys import stdin


input = stdin.readline
N = int(input())
square = [list(map(int, input().rstrip())) for _ in range(N)]

directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
ret = []

def dfs(x, y):
    cnt = 0  # 초기 카운트 = 0
    stack = [(x, y)]
    while stack:
        dx, dy = stack.pop()
        if square[dx][dy]:  # 만약 값이 1이라면,
            square[dx][dy] = 0  # 0으로 변경 후 카운트에 1 추가
            cnt += 1
            for dir_x, dir_y in directions:
                nx, ny = dx + dir_x, dy + dir_y
                if nx >= N or nx < 0 or ny >= N or ny < 0:  # NxN 범위를 벗어나면 무시
                    continue
                if square[nx][ny]:  # 방향값을 더한 좌표의 값이 1이라면,
                    stack.append((nx, ny))  # 스택에 추가
    return cnt

count = []

for i in range(N):
    for j in range(N):
        if square[i][j]:  # 값이 1이라면 dfs(i, j)실행, 결과값을 count에 추가.
            count.append(dfs(i, j))  # dfs를 한번 실행할때마다 해당 단지의 1들은 0으로 변경되므로 중복 X

print(len(count))

count.sort()
print(*count, sep="\n")