# 문제집 - 0x0D강 - 시뮬레이션


# 문제: https://www.acmicpc.net/problem/17142

# 비활성 바이러스는 빈칸으로 치지 않음. 활성화 되든 안되든 상관없음.
# 문제 설명 글👉 https://www.acmicpc.net/board/view/128517
# 반례 모음집👉 https://www.acmicpc.net/board/view/112928

# 메모리: 32412KB / 시간: 372ms
from sys import stdin


input = stdin.readline

N, M = map(int, input().split())
lab = []
virus = []
empty = 0

for i in range(N):
    line = list(map(int, input().split()))
    for j in range(N):
        if line[j] == 2:
            virus.append((i, j))
        elif line[j] == 0:
            empty += 1
    lab.append(line)


def bfs(comb):
    lab_copy = [line[:] for line in lab]
    curr = []
    cnt = 0
    total_time = 0
    
    for x, y in comb:
        curr.append((x, y, 0))
        lab_copy[x][y] = 1
    
    while curr:
        nxt = []
        for x, y, time in curr:
            for nx, ny in ((x-1, y), (x+1, y), (x, y-1), (x, y+1)):
                if 0 <= nx < N and 0 <= ny < N and lab_copy[nx][ny] != 1:
                    # 빈칸인 경우에만 total_time 업데이트
                    if lab_copy[nx][ny] == 0:
                        cnt += 1
                        total_time = time + 1
                    # 벽이 아니라면(0 또는 2)
                    if lab_copy[nx][ny] != 1:
                        nxt.append((nx, ny, time+1))
                        lab_copy[nx][ny] = 1
        curr = nxt
    return total_time if cnt == empty else N*N


ret = N*N

def dfs(start, comb):
    global ret

    if len(comb) == M:
        ret = min(bfs(comb), ret)
        return

    for i in range(start, len(virus)):
        comb.append(virus[i])
        dfs(i+1, comb)
        comb.pop()


# 빈칸이 0개일 경우 바이러스를 확산시킬 필요가 없으므로 바로 0 반환
if empty == 0:
    print(0)
else:
    dfs(0, [])
    print(ret if ret != N*N else -1)