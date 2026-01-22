# 구현
# 시뮬레이션


# 문제: https://www.acmicpc.net/problem/3227

# 🚨이전에 놓았던 돌이 꼭 "직전"에 놓았던 돌일 필요는 없음. 그냥 현재 전에 놓았던 돌이기만 하면 됨.
# 조건 관련 글: https://www.acmicpc.net/board/view/114167

# 메모리: 32412KB / 시간: 36ms
from sys import stdin


input = stdin.readline

def main():
    P, N = map(int, input().split())

    # 바둑판 상태 / 1: 깜돌, 0: 백돌
    board = [-1] * (P+1)

    for i in range(N):
        num = int(input())

        # 깜돌
        if i % 2:
            board[num] = 1

            # 현재 놓은 돌의 왼쪽, 오른쪽 탐색.
            # 이전에 놓았던 돌을 발견한다면 멈춤. 현재 돌-이전 돌 사이에 상대편 돌이 꽉 차있는지 체크한다.
            # -> 두 돌 사이 칸의 갯수 == 탐색하며 발견한 상대편 돌 갯수 라면 조건 만족.
            w_cnt = 0
            for j in range(num, 0, -1):
                if board[j] == 1:
                    if num - j - 1 == w_cnt:
                        board = board[:j+1] + [-1]*w_cnt + board[num:]
                        break
                if board[j] == 0:
                    w_cnt += 1
            
            w_cnt = 0
            for j in range(num, P+1):
                if board[j] == 1:
                    if j - num - 1 == w_cnt:
                        board = board[:num+1] + [-1]*w_cnt + board[j:]
                        break
                if board[j] == 0:
                    w_cnt += 1
        # 백돌
        else:
            board[num] = 0

            b_cnt = 0
            for j in range(num, 0, -1):
                if board[j] == 0:
                    if num - j - 1 == b_cnt:
                        board = board[:j+1] + [-1]*b_cnt + board[num:]
                        break
                if board[j] == 1:
                    b_cnt += 1
            
            b_cnt = 0
            for j in range(num, P+1):
                if board[j] == 0:
                    if j - num - 1 == b_cnt:
                        board = board[:num+1] + [-1]*b_cnt + board[j:]
                        break
                if board[j] == 1:
                    b_cnt += 1
    
    b = w = 0
    for num in board:
        if num == 0:
            w += 1
        elif num == 1:
            b += 1
    
    print(w, b)


main()