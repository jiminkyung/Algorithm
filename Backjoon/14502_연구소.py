# 문제집 - 0x0D강 - 시뮬레이션


# 문제: https://www.acmicpc.net/problem/14502

# 1. 조합 직접 구현
# 메모리: 34116KB / 시간: 1180ms
from sys import stdin
from collections import deque


input = stdin.readline

N, M = map(int, input().split())
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
lab = []
empty, virus = [], []
ret = 0

for i in range(N):
    line = list(map(int, input().split()))
    for j in range(M):
        if line[j] == 0:
            empty.append((i, j))
        elif line[j] == 2:
            virus.append((i, j))
    lab.append(line)

def bfs(comb):
    # 원본 lab 리스트 카피
    lab_copy = [line[:] for line in lab]
    queue = deque(virus)

    # 벽을 세울 좌표를 1로 변경해줌
    for idx in comb:
        x, y = empty[idx]
        lab_copy[x][y] = 1
    
    while queue:
        x, y = queue.popleft()

        for dx, dy in directions:
            nx, ny = x + dx, y + dy

            if 0 <= nx < N and 0 <= ny < M and lab_copy[nx][ny] == 0:
                lab_copy[nx][ny] = 2
                queue.append((nx, ny))
    
    cnt = 0
    for row in lab_copy:
        for col in row:
            if col == 0:
                cnt += 1
    return cnt

def combination(comb, start):
    global ret

    if len(comb) == 3:
        ret = max(ret, bfs(comb))
        return
    
    for i in range(start, len(empty)):
        comb.append(i)
        combination(comb, i+1)
        comb.pop()

combination([], 0)
print(ret)


# 2. combinations 모듈 사용
# 메모리: 34096KB / 시간: 1188ms
from sys import stdin
from collections import deque
from itertools import combinations


input = stdin.readline

N, M = map(int, input().split())
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
lab = []
empty, virus = [], []
ret = 0

for i in range(N):
    line = list(map(int, input().split()))
    for j in range(M):
        if line[j] == 0:
            empty.append((i, j))
        elif line[j] == 2:
            virus.append((i, j))
    lab.append(line)

def bfs(lab_copy):
    queue = deque(virus)

    while queue:
        x, y = queue.popleft()

        for dx, dy in directions:
            nx, ny = x + dx, y + dy

            if 0 <= nx < N and 0 <= ny < M and lab_copy[nx][ny] == 0:
                lab_copy[nx][ny] = 2
                queue.append((nx, ny))
    
    cnt = 0
    for row in lab_copy:
        for col in row:
            if col == 0:
                cnt += 1
    return cnt

for comb in combinations(empty, 3):
    # lab 카피본에 벽을 세울 좌표를 업데이트한 후 bfs() 실행
    lab_copy = [line[:] for line in lab]
    for r, c in comb:
        lab_copy[r][c] = 1
    ret = max(ret, bfs(lab_copy))

print(ret)