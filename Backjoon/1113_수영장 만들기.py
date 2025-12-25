# 구현
# 그래프 이론
# 그래프 탐색
# 시뮬레이션
# 너비 우선 탐색
# 격자 그래프


# 문제: https://www.acmicpc.net/problem/1113
# 구글링해본 문제... 힙을 사용하는게 가장 효율적인듯.
# 그냥 BFS만 이용해도 충분히 통과할 수 있을것같아서 BFS로 풀이.

# 나중에 다시 풀어봐야할 문제


# BFS 방식으로 푼 버전
# 메모리: 32544KB / 시간: 40ms
from sys import stdin


input = stdin.readline
INF = int(1e9)

def main():
    N, M = map(int, input().split())
    field = [tuple(map(int, input().rstrip())) for _ in range(N)]
    water = [[INF] * M for _ in range(N)]
    curr = []

    # 테두리 부분을 curr(큐 역할)에 미리 넣어주고 물 높이 기록.
    for col in range(M):
        curr.append((0, col))
        curr.append((N-1, col))
        water[0][col] = field[0][col]
        water[N-1][col] = field[N-1][col]
    
    for row in range(1, N-1):
        curr.append((row, 0))
        curr.append((row, M-1))
        water[row][0] = field[row][0]
        water[row][M-1] = field[row][M-1]
    

    def check(curr: list, N, M, water: list[list]) -> int:
        dx = [1, 0, -1, 0]
        dy = [0, -1, 0, 1]

        while curr:
            nxt = []
            for x, y in curr:
                for i in range(4):
                    nx, ny = x + dx[i], y + dy[i]

                    if not (0 <= nx < N and 0 <= ny < M):
                        continue

                    # water: 물이 찰 수 있는 최대 높이
                    # 인접 칸의 물 높이 = max(현재 칸 물 높이, 새 좌표의 벽 높이)
                    new_water = max(water[x][y], field[nx][ny])

                    # 새 좌표의 수면 높이
                    # 새 수면 높이가 기존 수면 높이보다 낮다면 갱신. (더 크면 흘러 넘치니까)
                    if new_water < water[nx][ny]:
                        water[nx][ny] = new_water
                        nxt.append((nx, ny))
            
            curr = nxt
        
        total = 0
        for i in range(N):
            for j in range(M):
                total += water[i][j] - field[i][j]
        
        return total
    

    print(check(curr, N, M, water))


main()