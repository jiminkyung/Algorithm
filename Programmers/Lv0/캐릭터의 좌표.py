# 강사님 방청소 버전으로 풀어보자 ㅎㅎ 간지났음
def solution(keyinput, board):
    path = {"up": (0, 1), "down": (0, -1), "left": (-1, 0), "right": (1, 0)}
    x, y = 0, 0
    max_x = (board[0]-1) // 2
    max_y = (board[1]-1) // 2

    for i in keyinput:
        dx, dy = path[i]
        nx, ny = x + dx, y + dy

        if -(max_x) <= nx <= max_x and -(max_y) <= ny <= max_y:
            x, y = nx, ny
    return [x, y]