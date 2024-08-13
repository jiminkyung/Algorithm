# 그래프와 순회

# 나이트가 이동할 수 있는 칸 = (+-)2행 1열 or 1행 2열.


# 메모리: 31884KB / 시간: 796ms

from sys import stdin


input = stdin.readline
T = int(input())
directions = [(-2, -1), (-2, 1), (2, -1), (2, 1),
              (-1, -2), (-1, 2), (1, -2), (1, 2)]

def bfs(sx, sy, ex, ey, size):
    board[sx][sy] = True
    curr = [(sx, sy)]
    count = 0

    while curr:
        nxt = []
        for x, y in curr:
            if x == ex and y == ey:
                return count
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < size and 0 <= ny < size and not board[nx][ny]:
                    board[nx][ny] = True
                    nxt.append((nx, ny))
        curr = nxt
        count += 1

for _ in range(T):
    I = int(input())
    board = [[False] * I for _ in range(I)]
    
    start_x, start_y = map(int, input().split())
    end_x, end_y = map(int, input().split())
    print(bfs(start_x, start_y, end_x, end_y, I))

# 굳이 큐에 추가하기 직전에 빙문체크를 하지 않아도 된다... 하지만 메모리 초과 오류가 발생함.
# 미로문제에서는 발생하지 않았음. 주어진 데이터 양의 차이일까?
# 고려해야할 방향의 수(미로: 4, 나이트: 8)의 차이로, 리스트에 쌓이는 데이터값이 너무 많아져서인듯.