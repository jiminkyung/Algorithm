# 구현
# 시뮬레이션


# 문제: https://www.acmicpc.net/problem/1531
# 메모리: 32412KB / 시간: 68ms
from sys import stdin


input = stdin.readline

def main():
    # 100x100 크기의 그림
    arr = [[0] * 100 for _ in range(100)]

    N, M = map(int, input().split())
    total = 0

    for _ in range(N):
        x1, y1, x2, y2 = map(lambda x: int(x) - 1, input().split())  # 0-based 처리

        # (x1, y1) ~ (x2, y2) 에 종이 추가
        for i in range(x1, x2 + 1):
            for j in range(y1, y2 + 1):
                # (i, j)의 그림이 아직 보이는 상태라면 종이 추가
                if arr[i][j] >= 0:
                    arr[i][j] += 1
                    # 종이 추가 후 가려진다면 카운트. 해당 좌표를 -1로 저장하여 다시 체크하지 않도록 함.
                    if arr[i][j] > M:
                        total += 1
                        arr[i][j] = -1

    print(total)


main()