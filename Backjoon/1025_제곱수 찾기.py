# 브루트포스 알고리즘


# 문제: https://www.acmicpc.net/problem/1025

# dx, dy 범위를 따로 설정할까 했는데, 질문 게시판에서 좋은 방법을 발견...
# 👉 https://www.acmicpc.net/board/view/75337
# 그냥 공차를 dx, dy 자체로 설정하면 편함. 생각하자...

# 메모리: 32412KB / 시간: 44ms
from sys import stdin


input = stdin.readline

def main():
    N, M = map(int, input().split())
    field = [input().rstrip() for _ in range(N)]
    
    max_num = -1  # 만들 수 없다면 -1을 출력

    # 1. 시작점이 될 좌표 (x, y) 설정
    for x in range(N):
        for y in range(M):
            # 🚨크기가 1x1인경우, 아래 dx == 0 and dy == 0 조건에 의해 제대로 계산되지 못함.
            # 이렇게 미리 계산해주거나, 질문 게시판처럼 dx, dy 범위를 (-N, N), (-M, M)으로 설정해주면 됨.

            # 단일 숫자(x, y)가 완전 제곱수인지 확인
            if int(int(field[x][y]) ** 0.5) ** 2 == int(field[x][y]):
                max_num = max(max_num, int(field[x][y]))
            # 2. 범위별로 공차 설정
            for dx in range(-N+1, N):
                for dy in range(-M+1, M):
                    if dx == 0 and dy == 0:  # 제자리에 머무는 경우는 제외
                        continue

                    # 3. 현재 시작점에서 특정 공차로 등차수열 만들기
                    num = field[x][y]
                    cx, cy = x + dx, y + dy

                    while 0 <= cx < N and 0 <= cy < M:
                        num += field[cx][cy]

                        if int(int(num) ** 0.5) ** 2 == int(num):
                            max_num = max(max_num, int(num))
                        cx += dx
                        cy += dy
    
    print(max_num)


main()