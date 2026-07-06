# 문제: https://school.programmers.co.kr/learn/courses/30/lessons/250125

def solution(board: list[list], h: int, w: int):
    cnt = 0
    N = len(board)
    val = board[h][w]
    for nx, ny in ((h+1, w), (h-1, w), (h, w+1), (h, w-1)):
        if 0 <= nx < N and 0 <= ny < N and board[nx][ny] == val:
            cnt += 1
    return cnt