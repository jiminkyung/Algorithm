# 문제집 - 대학생 기본반


# 문제: https://www.acmicpc.net/problem/1987

# 일반적인 백트래킹 풀이를 적용하면 Python3로 통과 X
# PyPy3로 통과된 코드.
# 메모리: 161728KB / 시간: 5052ms
from sys import stdin


input = stdin.readline

def dfs(x, y, visited, cnt):
    global max_cnt
    max_cnt = max(max_cnt, cnt)

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if 0 <= nx < R and 0 <= ny < C:
            idx = ord(board[nx][ny]) - 65
            if not visited[idx]:
                visited[idx] = True
                dfs(nx, ny, visited, cnt + 1)
                visited[idx] = False

R, C = map(int, input().split())
board = [input().rstrip() for _ in range(R)]

max_cnt = 0
visited = [False] * 26  # 알파벳 방문 여부
visited[ord(board[0][0]) - 65] = True
dfs(0, 0, visited, 1)

print(max_cnt)


# ⭐ set을 사용하면 Python3로 통과할 수 있다.
# 같은 코드로 list를 사용하면 시간초과. set을 사용해야만 함.
# 참고(질문게시판)👉 https://www.acmicpc.net/board/view/128382
# 참고(위 글에 링크된 블로그)👉 https://leeingyun96.tistory.com/22

# 메모리: 53644KB / 시간: 1200ms
from sys import stdin


input = stdin.readline

def dfs(board, alp, cnt):
    global ret
    stack = set()
    stack.add((0, 0, alp + board[0][0], cnt))

    while stack:
        cx, cy, alp, cnt = stack.pop()
        ret = max(ret, cnt)

        for nx, ny in ((cx+1, cy), (cx-1, cy), (cx, cy+1), (cx, cy-1)):
            if 0 <= nx < R and 0 <= ny < C and board[nx][ny] not in alp:
                stack.add((nx, ny, alp + board[nx][ny], cnt + 1))


R, C = map(int, input().split())
board = [input().rstrip() for _ in range(R)]

ret = 0
dfs(board, "", 1)
print(ret)

# ❗ 파라미터 없이 함수 내에서 변수선언을 하면 메모리는 줄고, 시간은 늘어난다.
# => ret을 전역 변수로 관리할 때는 그 값이 계속 유지되지만,
# 지역 변수로 관리할 경우 매번 pop한 값과 비교해야 하기 때문에 미묘한 시간 차이가 발생할 수 있음.
# 메모리: 51600KB / 시간: 1216ms
from sys import stdin


input = stdin.readline

def dfs(board):
    ret = 0
    stack = set()
    stack.add((0, 0, "" + board[0][0], 1))

    while stack:
        cx, cy, alp, cnt = stack.pop()
        ret = max(ret, cnt)

        for nx, ny in ((cx+1, cy), (cx-1, cy), (cx, cy+1), (cx, cy-1)):
            if 0 <= nx < R and 0 <= ny < C and board[nx][ny] not in alp:
                stack.add((nx, ny, alp + board[nx][ny], cnt + 1))
    return ret


R, C = map(int, input().split())
board = [input().rstrip() for _ in range(R)]
print(dfs(board))