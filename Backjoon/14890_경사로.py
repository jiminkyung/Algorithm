# 문제집 - 0x0D강 - 시뮬레이션


# 문제: https://www.acmicpc.net/problem/14890
# 메모리: 31120KB / 시간: 44ms
from sys import stdin


input = stdin.readline

N, L = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]
graph_reversed = list(map(list, zip(*graph)))  # 행렬 뒤집기

def checking(line):
    visited = [False] * N

    for i in range(1, N):
        # 높이 차이가 1인지 확인
        if abs(line[i] - line[i-1]) > 1:
            return False
        if line[i] == line[i-1]:
            continue

        if line[i] == line[i-1] + 1:
            for j in range(i-1, i-L-1, -1):  # 전 위치에서부터 -L까지
                # 범위 밖이거나, 높이가 다르거나, 이미 경사로를 놓았다면
                if j < 0 or line[j] != line[i-1] or visited[j]:
                    return False
                visited[j] = True
        elif line[i] == line[i-1] - 1:
            for j in range(i, i+L):  # 현재 위치에서부터 +L까지
                if j >= N or line[j] != line[i] or visited[j]:
                    return False
                visited[j] = True
    return True

total_cnt = 0
for i in range(N):
    total_cnt += checking(graph[i])
    total_cnt += checking(graph_reversed[i])

print(total_cnt)