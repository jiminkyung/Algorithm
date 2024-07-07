# 백트래킹
# AI선생님과 함께한 풀이.
# 이 문제도 보통의 풀이로는 통과 X, 비트마스킹을 이용한 풀이로 통과함.

# 메모리: 31120KB / 시간: 3464ms

import sys


def solve_sudoku(board):
    rows = [0] * 9
    cols = [0] * 9
    boxes = [0] * 9
    empty = []

    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                empty.append((i, j))
            else:
                num = board[i][j]
                rows[i] |= 1 << num
                cols[j] |= 1 << num
                boxes[(i//3)*3 + j//3] |= 1 << num

    def backtrack(index):
        if index == len(empty):
            return True

        i, j = empty[index]
        box = (i//3)*3 + j//3  # 해당 index가 속한 박스의 번호
        for num in range(1, 10):
            if not (rows[i] & (1 << num)) and not (cols[j] & (1 << num)) and not (boxes[box] & (1 << num)):
                board[i][j] = num
                rows[i] |= 1 << num
                cols[j] |= 1 << num
                boxes[box] |= 1 << num

                if backtrack(index + 1):
                    return True

                board[i][j] = 0
                rows[i] &= ~(1 << num)
                cols[j] &= ~(1 << num)
                boxes[box] &= ~(1 << num)

        return False

    backtrack(0)

board = [list(map(int, sys.stdin.readline().split())) for _ in range(9)]

solve_sudoku(board)

for row in board:
    sys.stdout.write(" ".join(str(r) for r in row)+"\n")