# 문제집 - 0x09강 - BFS


# 문제: https://www.acmicpc.net/problem/1600

# 푸는 방식 자체는 정답과 비슷한데 자꾸 오답이 나와서 다른 풀이를 참고했다.
# 참고👉 https://2hs-rti.tistory.com/entry/%EB%B0%B1%EC%A4%80-1600%EB%B2%88-%EB%A7%90%EC%9D%B4-%EB%90%98%EA%B3%A0%ED%94%88-%EC%9B%90%EC%88%AD%EC%9D%B4-%ED%8C%8C%EC%9D%B4%EC%8D%AC

# 말의 이동방식을 사용하는 경우의 수(K)를 저장할 배열을 하나 더 만들어야 한다.
# 메모리: 49908KB / 시간: 2700ms
from sys import stdin
from collections import deque


input = stdin.readline

def bfs():
    queue = deque([(0, 0, K)])
    # visited[x][y][k]로 3차원 배열 생성
    visited = [[[-1] * (K+1) for _ in range(W)] for _ in range(H)]
    visited[0][0][K] = 0

    while queue:
        x, y, k = queue.popleft()

        if x == H-1 and y == W-1:
            return visited[x][y][k]
        
        if k > 0:  # 아직 말의 움직임으로 이동할 수 있는 횟수가 남아있다면
            for i in range(8):
                nx = x + horse_dx[i]
                ny = y + horse_dy[i]
                if 0 <= nx < H and 0 <= ny < W:
                    if graph[nx][ny] != 1 and visited[nx][ny][k-1] == -1:
                        visited[nx][ny][k-1] = visited[x][y][k] + 1
                        queue.append((nx, ny, k-1))
        
        # 가능 여부와 상관없이 원숭이의 움직임으로는 항상 이동 가능
        for i in range(4):
            nx = x + monkey_dx[i]
            ny = y + monkey_dy[i]
            if 0 <= nx < H and 0 <= ny < W:
                if graph[nx][ny] != 1 and visited[nx][ny][k] == -1:
                    visited[nx][ny][k] = visited[x][y][k] + 1
                    queue.append((nx, ny, k))
    return -1


K = int(input())
W, H = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(H)]
monkey_dx = [0, 1, 0, -1]
monkey_dy = [1, 0, -1, 0]
horse_dx = [-2, -1, 1, 2, 2, 1, -1, -2]
horse_dy = [1, 2, 2, 1, -1, -2, -2, -1]

print(bfs())