# 문제집 - 0x09강 - BFS


# 문제: https://www.acmicpc.net/problem/1926
# '그림이 없을경우 최대값은 0이 된다' 가 조건이다. 문제를 끝까지 읽자...

# 메모리: 34932KB / 시간: 340ms
from sys import stdin
from collections import deque


input = stdin.readline

def bfs(x, y):
    queue = deque([(x, y)])
    visited[x][y] = 0
    cnt = 1

    while queue:
        cx, cy = queue.popleft()
        for nx, ny in ((cx-1, cy), (cx+1, cy), (cx, cy-1), (cx, cy+1)):
            if 0 <= nx < n and 0 <= ny < m and visited[nx][ny]:
                visited[nx][ny] = 0
                queue.append((nx, ny))
                cnt += 1
    return cnt


n, m = map(int, input().split())
# 어차피 1, 0으로 주어지므로 주어진 입력값들을 그대로 방문체크 리스트로 사용.
visited = [list(map(int, input().split())) for _ in range(n)]
ret = []

for i in range(n):
    for j in range(m):
        if visited[i][j]:
            ret.append(bfs(i, j))

if ret:
    print(len(ret), max(ret), sep="\n")
else:
    print(0, 0, sep="\n")