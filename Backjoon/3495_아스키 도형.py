# 구현
# 기하학
# 홀짝성


# 문제: https://www.acmicpc.net/problem/3495
# 메모리: 32412KB / 시간: 36ms
from sys import stdin


input = stdin.readline

def main():
    h, w = map(int, input().split())
    arr = [input().rstrip() for _ in range(h)]

    # 각 줄마다 검사.
    # 대각선 /, \ 중 아무거나 상관없이,
    # 현재까지 홀수개가 나온 상태면 선분이 끝나지 않은 상태.
    # 짝수개가 나온 상태면 끝난 상태(앞에서 나온 대각선과 교합된 상태).
    area = 0

    # (i, j)의 해당하는 칸이 대각선이라면 1, 아니라면 홀짝성 판단.
    # 홀수라면 도형의 칸으로 간주하고 2를 더해줌, 짝수라면 빈칸이므로 넘어감.
    for i in range(h):
        cnt = 0
        for j in range(w):
            if arr[i][j] != ".":
                cnt += 1
                area += 1
            else:
                if cnt % 2 != 0:
                    area += 2
    
    # 2배씩 더해준 상태이므로 마지막에 // 2 처리해주기.
    print(area // 2)


main()