# 구현
# 브루트포스 알고리즘
# 시뮬레이션


# 문제: https://www.acmicpc.net/problem/3258
# 메모리: 32412KB / 시간: 28ms
from sys import stdin


input = stdin.readline

def main():
    # N: 필드 수, Z: 도착 지점, M: 장애물 수
    N, Z, M = map(int, input().split())
    field = [0] * N

    for M in map(int, input().split()):
        num = M - 1  # 0-based 처리
        field[num] = 1
    
    def check(K: int) -> bool:
        idx = 0
        visited = [False] * N

        while idx != Z-1:
            idx = (idx + K) % N

            # 장애물이 있거나 이미 방문한 좌표라면 -> 도달 불가
            if field[idx] or visited[idx]:
                return False
            visited[idx] = True  # 방문 처리
        return True
    
    # K: 한번에 이동 가능한 칸
    # 어차피 N칸 이상 이동하는건 의미 없으므로, 1칸 ~ N-1칸 까지를 K 범위로 잡음.
    for K in range(1, N):
        if check(K):
            print(K)
            break


main()