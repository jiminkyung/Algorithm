# 문제집 - 대학생 기본반


# 문제: https://www.acmicpc.net/problem/2583
# 메모리: 31120KB / 시간: 36ms
from sys import stdin


def bfs(x, y):
    curr = [(x, y)]
    visited[x][y] = True
    cnt = 1

    while curr:
        nxt = []
        for cx, cy in curr:
            for nx, ny in ((cx-1, cy), (cx+1, cy), (cx, cy-1), (cx, cy+1)):
                if 0 <= nx < M and 0 <= ny < N and not visited[nx][ny]:
                    visited[nx][ny] = True
                    nxt.append((nx, ny))
                    cnt += 1
        curr = nxt
    return cnt

input = stdin.readline

M, N, K = map(int, input().split())
visited = [[False] * N for _ in range(M)]
ret = []

for _ in range(K):
    x1, y1, x2, y2 = map(int, input().split())
    # MxN 기준 행렬로 치환하면 범위는 (M-y2, x1) ~ (M-y2 + y증가량 - 1, x1 + x증가량 - 1)이 된다.
    # for문 범위는 종료값-1 까지이므로 (M-y2 + y증가량), (x1 + x증가량)까지만 계산해줘도 됨.
    for i in range(M-y2, M-y2 + (y2-y1)):
        for j in range(x1, x1 + (x2-x1)):
            visited[i][j] = True

for i in range(M):
    for j in range(N):
        if not visited[i][j]:
            ret.append(bfs(i, j))

ret.sort()
print(len(ret))
print(*ret)