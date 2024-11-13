# 문제집 - 0x09강 - BFS


# 문제: https://www.acmicpc.net/problem/9328
# 11967_불켜기 문제와 비슷한 느낌이 있다. 물론 조건, 입력값으로 주어지는 데이터 자체가 틀리기 때문에 같은 문제는 X

# 메모리: 34148KB / 시간: 112ms
from sys import stdin
from collections import deque, defaultdict


input = stdin.readline
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def bfs(h, w, key):
    keys = set(key)
    if keys == {"0"}:
        keys = set()
    
    visited = [[False] * w for _ in range(h)]
    queue = deque()
    waiting = defaultdict(list)  # 키가 없어서 열지 못했던 문들
    doc = 0

    for i in range(h):
        for j in range(w):
            if (i in (0, h-1) or j in (0, w-1)) and building[i][j] != "*":
                visited[i][j] = True
                queue.append((i, j))
    
    while queue:
        x, y = queue.popleft()
        curr = building[x][y]

        # 문서일경우 빈 공간으로 바꿔주고 결과값 업데이트
        if curr == "$":
            doc += 1
            building[x][y] = "."
        # 소문자(키)라면 키 리스트에 추가, 빈 공간으로 변경
        elif "a" <= curr <= "z":
            if curr not in keys:
                keys.add(curr)
                # 해당 문의 대기리스트를 큐에 추가(이제 열 수 있으므로)
                for wx, wy in waiting[curr.upper()]:
                    queue.append((wx, wy))
                # 큐에 추가 후 해당 문의 대기리스트는 비워준다.
                waiting[curr.upper()] = []
            building[x][y] = "."
        # 대문자(문)라면 키가 존재하는지 체크
        elif "A" <= curr <= "Z":
            if curr.lower() not in keys:
                # 키를 갖고있지 않는 상태라면 대기 리스트에 추가
                waiting[curr].append((x, y))
                continue
        
        for dx, dy in directions:
            nx, ny = dx + x, dy + y
            # 벽이 아니고 방문하지 않았던 경로라면
            if 0 <= nx < h and 0 <= ny < w and not visited[nx][ny]:
                if building[nx][ny] != "*":
                    visited[nx][ny] = True
                    queue.append((nx, ny))
    return doc


for _ in range(int(input())):
    h, w = map(int, input().split())
    building = [list(input().rstrip()) for _ in range(h)]
    key = input().rstrip()
    print(bfs(h, w, key))