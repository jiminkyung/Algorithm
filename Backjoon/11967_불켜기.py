# 문제집 - 0x09강 - BFS


# 문제: https://www.acmicpc.net/problem/11967
# 다시 풀어볼만한 문제인것같다!

# 1. 현재 방에서 켤 수 있는 스위치는 모두 켠다.
# => 만약 스위치를 켠 방 주위로 이미 방문한 방이 있다면 큐에 추가.
# 2. 현재 방 주위로 불이 켜져있으나 아직 방문하지 않은 방이 있다면 큐에 추가.

# 메모리: 35028KB / 시간: 100ms
from sys import stdin
from collections import deque, defaultdict


input = stdin.readline


def bfs():
    queue = deque([(0, 0)])
    visited = [[False] * N for _ in range(N)]
    visited[0][0] = True
    lit_rooms = set()
    lit_rooms.add((0, 0))
    light = 1

    while queue:
        x, y = queue.popleft()

        for a, b in board[(x, y)]:
            if (a, b) not in lit_rooms:
                lit_rooms.add((a, b))
                light += 1
                for dx, dy in directions:
                    nx, ny = dx + a, dy + b
                    if 0 <= nx < N and 0 <= ny < N and visited[nx][ny]:
                        queue.append((nx, ny))
        
        for dx, dy in directions:
            nx, ny = dx + x, dy + y
            if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny]:
                if (nx, ny) in lit_rooms:
                    visited[nx][ny] = True
                    queue.append((nx, ny))
    return light

N, M = map(int, input().split())
directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

board = defaultdict(list)
for _ in range(M):
    x, y, a, b = map(int, input().split())
    board[(x-1, y-1)].append((a-1, b-1))

print(bfs())


# 🌟 그냥 불을 켠 방 자체를 큐에 넣는게 더 효율적이지 않을까? 싶어서 수정한 결과.
# => 불을 켠 방을 방문체크 후 바로 큐에 삽입.

# 메모리: 35328KB / 시간: 92ms
from sys import stdin
from collections import deque, defaultdict


input = stdin.readline

def bfs():
    queue = deque([(0, 0)])
    visited = [[False] * N for _ in range(N)]
    visited[0][0] = True
    lit_rooms = set()
    lit_rooms.add((0, 0))
    light = 1

    while queue:
        x, y = queue.popleft()

        for a, b in board[(x, y)]:
            if (a, b) not in lit_rooms:
                lit_rooms.add((a, b))
                light += 1
                for dx, dy in directions:
                    nx, ny = dx + a, dy + b
                    if 0 <= nx < N and 0 <= ny < N and visited[nx][ny]:
                        queue.append((a, b))
                        visited[a][b] = True
                        break
        
        for dx, dy in directions:
            nx, ny = dx + x, dy + y
            if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny]:
                if (nx, ny) in lit_rooms:
                    visited[nx][ny] = True
                    queue.append((nx, ny))
    return light

N, M = map(int, input().split())
directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

board = defaultdict(list)
for _ in range(M):
    x, y, a, b = map(int, input().split())
    board[(x-1, y-1)].append((a-1, b-1))

print(bfs())