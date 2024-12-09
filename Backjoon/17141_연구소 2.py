# 문제집 - 0x0D강 - 시뮬레이션


# 문제: https://www.acmicpc.net/problem/17141
# 메모리: 32544KB / 시간: 328ms
from sys import stdin


input = stdin.readline

N, M = map(int, input().split())
virus = []
lab = []
empty = -M  # 빈칸 0의 갯수. M개는 항상 시발점이므로 미리 감해줌.
ret = int(1e9)

def bfs(comb, cnt):
    lab_copy = [line[:] for line in lab]
    curr = []

    for x, y in comb:
        curr.append((x, y, 0))
        lab_copy[x][y] = 1
    
    while curr:
        nxt = []
        for x, y, time in curr:
            for nx, ny in ((x-1, y), (x+1, y), (x, y-1), (x, y+1)):
                if nx < 0 or nx >= N or ny < 0 or ny >= N:
                    continue
                if lab_copy[nx][ny] != 1:
                    lab_copy[nx][ny] = 1
                    nxt.append((nx, ny, time+1))
                    cnt -= 1
        curr = nxt
    if cnt == 0:
        return time
    return -1


comb = []

def dfs(start, comb):
    global ret

    if len(comb) == M:
        t = bfs(comb, empty)
        if t != -1:
            ret = min(ret, t)
        return
    
    for i in range(start, len(virus)):
        comb.append(virus[i])
        dfs(i+1, comb)
        comb.pop()


for i in range(N):
    line = list(map(int, input().split()))
    for j in range(N):
        if line[j] == 2:
            virus.append((i, j))
            empty += 1
        elif line[j] == 0:
            empty += 1
    lab.append(line)

dfs(0, [])
print(ret if ret != int(1e9) else -1)