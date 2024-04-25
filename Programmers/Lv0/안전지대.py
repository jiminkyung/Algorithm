# for+if 덩어리가 되길래 포기했다...
# 아래는 좋아요 수가 제일 많았던 파이썬 풀이.
def solution(board):
    n = len(board)
    danger = set()
    for i, row in enumerate(board):
        for j, x in enumerate(row):
            if not x:
                continue
            danger.update((i+di, j+dj) for di in [-1,0,1] for dj in [-1, 0, 1])
    return n*n - sum(0 <= i < n and 0 <= j < n for i, j in danger)

# 이게 Lv0이 맞냐?!