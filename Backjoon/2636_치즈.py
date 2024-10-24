# 문제집 - BOJ 길라잡이 베타 (1)


# 문제: https://www.acmicpc.net/problem/2636
# 참고👉 https://velog.io/@hygge/Python-%EB%B0%B1%EC%A4%80-2636-%EC%B9%98%EC%A6%88-BFS

# 메모리: 34096KB / 시간: 68ms
from sys import stdin
from collections import deque


input = stdin.readline

def bfs(visited):
    queue = deque([(0, 0)])
    melted = deque([])

    while queue:
        x, y = queue.popleft()

        for nx, ny in ((x-1, y), (x+1, y), (x, y-1), (x, y+1)):
            if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny]:
                visited[nx][ny] = True
                if cheeze[nx][ny] == 0:
                    queue.append((nx, ny))
                else:
                    melted.append((nx, ny))
    
    # 치즈를 한번에 녹여야 함. 위에서 cheeze[nx][ny] = 0 으로 변경하면 현재 테두리를 탐색할 수 없음.
    for x, y in melted:
        cheeze[x][y] = 0
    return len(melted)

N, M = map(int, input().split())

cheeze = [list(map(int, input().split())) for _ in range(N)]
cnt = sum(sum(line) for line in cheeze)
time = 0

while cnt != 0:
    time += 1
    visited = [[False] * M for _ in range(N)]
    melted_cnt = bfs(visited)
    cnt -= melted_cnt

    if cnt == 0:
        print(time, melted_cnt, sep="\n")