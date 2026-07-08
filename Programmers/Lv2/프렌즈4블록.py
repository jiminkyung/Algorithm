# 문제: https://school.programmers.co.kr/learn/courses/30/lessons/17679

def solution(m: int, n: int, board: list[str]) -> int:
    board = [list(board[i]) for i in range(m)]  # 원소 변경을 위해 문자열을 문자들로 분리.
    dx = [0, 0, 1, 1]
    dy = [0, 1, 0, 1]
    found = True
    cnt = 0
    
    while found:
        new_board = [board[i][:] for i in range(m)]
        found = False
        
        for x in range(m-1):
            for y in range(n-1):
                if board[x][y]:  # 0이 아닐경우
                    if sum(board[x][y] == board[x+dx[i]][y+dy[i]] for i in range(4)) == 4:
                        for i in range(4):
                            new_board[x+dx[i]][y+dy[i]] = 0
                        found = True
        
        if found:  # 폭파된 부분이 있다면 board 갱신
            board = [new_board[i][:] for i in range(m)]
            
            # 빈 공간이 남지 않게 아래로 떨어뜨리기
            for y in range(n):
                for x in range(m-2, -1, -1):  # 아래에서 위 방향으로 진행
                    if board[x][y]:
                        nx = x+1  # nx: 현재 값과 swap할 위치
                        while nx < m and board[nx][y] == 0:
                            nx += 1
                        board[x][y], board[nx-1][y] = board[nx-1][y], board[x][y]

    cnt += sum(sum(board[i][j] == 0 for j in range(n)) for i in range(m))
    return cnt