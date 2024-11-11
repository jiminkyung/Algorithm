# 문제집 - 0x09강 - BFS


# 문제: https://www.acmicpc.net/problem/16920
# Si만큼 이동한다는게, 현좌표에서 +- Si 만큼이 아니라 현좌표에서 1씩 이동하는것을 총 Si만큼 할수있다는뜻이다.

# 현좌표에서 +- Si 로 이해하고 작성한 코드... 당연히 오답. 제출도 안했다.
from sys import stdin
from collections import deque


input = stdin.readline

def bfs():
    while queue:
        x, y, p = queue.popleft()
        d = S[p]

        for nx, ny in ((x-d, y), (x+d, y), (x, y-d), (x, y+d)):
            if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny]:
                visited[nx][ny] = True
                score[p] += 1
                queue.append((nx, ny, p))


N, M, P = map(int, input().split())
# S = {str(i): s for i, s in enumerate(map(int, input().split()), 1)}
S = [0] + list(map(int, input().split()))

board = [input().rstrip() for _ in range(N)]
visited = [[False] * M for _ in range(N)]
queue = deque([])

score = [0] + [1] * P
player = [i for i in range(P, 0, -1)]

for i in range(N):
    for j in range(M):
        if board[i][j] == "#":
            visited[i][j] = True
        elif board[i][j] == str(player[-1]):
            visited[i][j] = True
            queue.append((i, j, player[-1]))
            player.pop()

bfs()

print(*score[1:])


# ⭐ 해결포인트는 각 선수마다 deque를 생성해주는 것이었음. 생각보다 간단하다.
# 참고👉 https://puleugo.tistory.com/85
# 참고2👉 https://door-of-tabris.tistory.com/entry/%EB%B0%B1%EC%A4%80-16920%EB%B2%88-%ED%99%95%EC%9E%A5%EA%B2%8C%EC%9E%84%ED%8C%8C%EC%9D%B4%EC%8D%AC

# 메모리: 124700KB / 시간: 1444ms
from sys import stdin
from collections import deque


input = stdin.readline

def bfs():
    is_moved = True

    while is_moved:
        is_moved = False

        for i in range(1, P+1):
            if not castle[i]:
                continue

            queue = castle[i]
            for _ in range(S[i]):
                
                for _ in range(len(queue)):
                    x, y = queue.popleft()
                    for nx, ny in ((x-1, y), (x+1, y), (x, y-1), (x, y+1)):
                        if 0 <= nx < N and 0 <= ny < M and board[nx][ny] == ".":
                            board[nx][ny] = str(i)
                            score[i] += 1
                            queue.append((nx, ny))
                            is_moved = True


N, M, P = map(int, input().split())
S = [0] + list(map(int, input().split()))

board = [list(input().rstrip()) for _ in range(N)]

score = [0] * (P+1)  # 선수가 소유한 성의 갯수
castle = [deque() for _ in range(P+1)]  # 각 선수가 가진 성의 좌표

for i in range(N):
    for j in range(M):
        b = board[i][j]

        # visited 따로 생성 X, 숫자일경우 선수로 판단
        if b != "#" and b != ".":
            score[int(b)] += 1
            castle[int(b)].append((i, j))

bfs()

print(*score[1:])