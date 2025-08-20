# 구현


# 문제: https://www.acmicpc.net/problem/1986
# 메모리: 39332KB / 시간: 108ms
from sys import stdin


input = stdin.readline

def main():
    n, m = map(int, input().split())
    queen = list(map(int, input().split()))
    night = list(map(int, input().split()))
    pawn = list(map(int, input().split()))
    # 0: 기물, 1: 방문
    field = [[-1] * m for _ in range(n)]
    # 안전한 칸
    cnt = n*m

    def check(horse: list) -> list[tuple]:
        """ 해당 기물의 좌표 저장, 기물 위치 체크 """
        nonlocal field, cnt

        horses = []
        
        for i in range(1, horse[0]*2, 2):
            x, y = horse[i]-1, horse[i+1]-1
            field[x][y] = 0
            cnt -= 1
            horses.append((x, y))
        return horses
    

    # 1. 각 기물의 좌표 저장, 위치 체크
    queens = check(queen)
    nights = check(night)
    _ = check(pawn)  # 폰은 장애물 역할만 함

    
    def queen_move(queens: list):
        nonlocal field, cnt

        # 가로, 세로, 대각선 방향으로 이동
        dx = [1, 0, -1, 0, -1, -1, 1, 1]
        dy = [0, -1, 0, 1, 1, -1, 1, -1]
        
        for bx, by in queens:
            for d in range(8):
                x, y = bx, by
                while True:  # 퀸은 장애물을 만나기 전까진 계속 이동할 수 있음
                    nx = x + dx[d]
                    ny = y + dy[d]

                    # 판을 벗어나거나 장애물(기물)이 있다면 해당 방향으로 이동 중지.
                    # 아니라면 해당 방향으로 계속 이동.
                    if not (0 <= nx < n and 0 <= ny < m) or field[nx][ny] == 0:
                        break
                    # 표시가 안된 좌표라면 체크 후 카운트
                    if field[nx][ny] == -1:
                        field[nx][ny] = 1
                        cnt -= 1
                    
                    x, y = nx, ny
    

    def night_move(nights: list):
        nonlocal field, cnt

        # L자 모양으로 이동
        dx = [-2, -2, 2, 2, -1, -1, 1, 1]
        dy = [-1, 1, -1, 1, -2, 2, -2, 2]

        for bx, by in nights:
            # 각 방향으로 한번씩만 이동
            for d in range(8):
                nx = bx + dx[d]
                ny = by + dy[d]

                # 판을 벗어나거나 해당 좌표에 장애물(기물)이 있다면 이동 중지.
                # => 장애물을 뛰어넘을순 있으나 도착하려는 좌표에 장애물이 있어선 안됨.
                if not (0 <= nx < n and 0 <= ny < m) or field[nx][ny] == 0:
                    continue

                if field[nx][ny] == -1:
                    field[nx][ny] = 1
                    cnt -= 1


    # 2. 기물 이동
    queen_move(queens)
    night_move(nights)

    print(cnt)


main()