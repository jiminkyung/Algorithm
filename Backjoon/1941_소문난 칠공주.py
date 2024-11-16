# 문제집 - 0x0C강 - 백트래킹


# 문제: https://www.acmicpc.net/problem/1941
# 백트래킹 연습을 많이 해야할듯하다 ㅜㅜ

# 메모리: 34072KB / 시간: 1512ms
from sys import stdin
from collections import deque

input = stdin.readline

place = [input().rstrip() for _ in range(5)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
ret = 0

def bfs(team):
    """
    team의 첫번째 학생을 큐와 seen(set)에 추가한다.
    첫번째 학생으로부터 bfs를 진행하며 조건을 체크한다.
    조건은 1) 방문하지 않은 좌표일것(seen으로 체크), 2) team에 존재하는 좌표일것
    두 조건을 만족한다면 seen, 큐에 해당 좌표를 추가하고 카운트한다.
    최종 카운트가 7이라면 True, 아니라면 False를 반환하게 된다.
    """
    queue = deque([team[0]])
    seen = {team[0]}  # set()
    cnt = 1

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if (nx, ny) in team and (nx, ny) not in seen:
                seen.add((nx, ny))
                queue.append((nx, ny))
                cnt += 1
    return cnt == 7

def dfs(start, cnt, s_cnt, team):
    """
    일단 7명이 될 때까지 반복한다.
    만약 이다솜파가 4명 이상이고, bfs(연결되어있음)를 만족하면 최종 결과값을 카운트한다.
    """
    global ret

    if cnt == 7:
        if s_cnt >= 4 and bfs(team):
            ret += 1
        return

    for i in range(start, 25):
        r, c = divmod(i, 5)  # r = i // 5, c = i % 5
        team.append((r, c))
        dfs(i + 1, cnt + 1, s_cnt + (place[r][c] == "S"), team)
        team.pop()

dfs(0, 0, 0, [])
print(ret)