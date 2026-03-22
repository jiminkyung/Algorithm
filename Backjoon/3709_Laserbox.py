# 구현
# 그래프 이론
# 그래프 탐색
# 시뮬레이션


# 문제: https://www.acmicpc.net/problem/3709
# 메모리: 32412KB / 시간: 32ms
from sys import stdin


input = stdin.readline

def main():
    T = int(input())

    for _ in range(T):
        print(*solve())


def solve() -> tuple[int, int]:
    N, R = map(int, input().split())
    # (x, y)좌표를 배열에 맞게 변환 후, 해당 위치에 우회전기가 존재할경우 1로 변경.
    arr = [[0] * N for _ in range(N)]

    for _ in range(R):
        x, y = map(int, input().split())
        # 0-indexed 기준으로 맞추기
        arr[N-y][x-1] = 1
    
    rx, ry = map(int, input().split())
    # 좌표 기준으로 북, 동, 남, 서
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    d = 0

    # (x, 0): 남쪽 경계에 위치. 레이저 방향은 ↑ 북
    # (x, N+1): 북쪽 경계에 위치. 레이저 방향은 ↓ 남
    # (0, y): 서쪽 경계에 위치. 레이저 방향은 → 동
    # (N+1, y): 동쪽 경계에 위치. 레이저 방향은 ← 서
    if rx == 0 or rx == N+1:
        d = 1 if rx == 0 else 3
    else:
        d = 0 if ry == 0 else 2
    
    # 일단 한 칸 이동시켜서 판 안에 위치하게끔 만들어줌.
    rx += dx[d]
    ry += dy[d]

    while 0 < rx <= N and 0 < ry <= N:
        # 우회전기가 존재하는 칸이라면 우회전
        if arr[N-ry][rx-1]:
            d = (d + 1) % 4
        
        rx += dx[d]
        ry += dy[d]
    
    return rx, ry


main()