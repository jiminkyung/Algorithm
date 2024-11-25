# 문제집 - 0x0D강 - 시뮬레이션


# 문제: https://www.acmicpc.net/problem/15685
# 메모리: 31120KB / 시간: 44ms
from sys import stdin


input = stdin.readline

N = int(input())
# 100x100 격자이므로 행렬은 101개씩 생성
graph = [[0] * 101 for _ in range(101)]
directions = [(0, 1), (-1, 0), (0, -1), (1, 0)]
curved = set()  # 드래곤 커브가 생성된 좌표


def curve(g, curr, path):
    if g == curr:
        return path
    # 다음 세대의 경로 = 기존 경로를 뒤집은 다음 90º씩 회전
    # 다음 세대의 시작점은 현재 세대의 끝점이기 때문에 뒤집어줘야함.
    new_path = [(p+1) % 4 for p in reversed(path)]
    return curve(g, curr+1, path + new_path)


def checking(y, x, path):
    for p in path:
        ny, nx = y + directions[p][0], x + directions[p][1]
        graph[ny][nx] = 1
        curved.add((ny, nx))
        y, x = ny, nx


for _ in range(N):
    x, y, d, g = map(int, input().split())
    # 0세대부터 g세대까지의 방향 변화를 저장
    path = curve(g, 0, [d])
    graph[y][x] = 1
    curved.add((y, x))
    checking(y, x, path)

ret = 0

for i in range(100):
    for j in range(100):
        if (i, j) in curved and (i+1, j) in curved and (i, j+1) in curved and (i+1, j+1) in curved:
            ret += 1

print(ret)