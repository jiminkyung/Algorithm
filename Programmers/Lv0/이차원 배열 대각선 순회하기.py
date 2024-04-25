def solution(board, k):
    ret = 0
    for i in range(len(board)):
        for j in range(len(board[i])):
            if i + j <= k:
                ret += board[i][j]
    return ret