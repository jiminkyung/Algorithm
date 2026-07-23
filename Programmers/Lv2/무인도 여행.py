# 문제: https://school.programmers.co.kr/learn/courses/30/lessons/154540

def solution(maps: list[str]):
    N, M = len(maps), len(maps[0])
    visited = [[False] * M for _ in range(N)]
    ret = []

    def bfs(x, y) -> int:
        visited[x][y] = True
        food = int(maps[x][y])  # 현재 칸 (x, y)의 값으로 초기화
        curr = [(x, y)]
        dx = [1, 0, -1, 0]
        dy = [0, 1, 0, -1]

        while curr:
            nxt = []

            for x, y in curr:
                for i in range(4):
                    nx, ny = x + dx[i], y + dy[i]

                    if not (0 <= nx < N and 0 <= ny < M) or visited[nx][ny]:
                        continue

                    # 숫자일 경우에만 이동, food 갱신.
                    if maps[nx][ny].isdigit():
                        food += int(maps[nx][ny])
                        visited[nx][ny] = True
                        nxt.append((nx, ny))
            
            curr = nxt[:]
        
        return food
    

    for x in range(N):
        for y in range(M):
            if not visited[x][y] and maps[x][y].isdigit():
                ret.append(bfs(x, y))
    
    return sorted(ret) if ret else [-1]