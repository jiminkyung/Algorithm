# 구현
# 시뮬레이션


# 문제: https://www.acmicpc.net/problem/3254

# 구현 연습하기 좋은 문제
# 메모리: 32412KB / 시간: 36ms
from sys import stdin


input = stdin.readline

def main():
    print(solve())


def solve():
    arr = [[-1] * 7 for _ in range(6)]
    data = [tuple(map(lambda x: int(x) - 1, input().split())) for _ in range(21)]

    def check(c: int, p: int) -> int:
        """ c: 열, p: 플레이어(상근 0/정인 1) """
        # 상하 / 좌우 / 좌상우하 / 우상좌하
        dx = [-1, 1, 0, 0, -1, 1, -1, 1]
        dy = [0, 0, -1, 1, -1, 1, 1, -1]
        x, y = -1, c

        # 김밥 떨어뜨리기
        for i in range(5, -1, -1):
            if arr[i][c] == -1:
                arr[i][c] = p
                x = i
                break
        
        # 위에 나눈 네 방향으로 검사 진행
        for i in range(0, 8, 2):
            cnt = 0  # 현재 방향에 존재하는 p의 김밥 갯수
            for j in range(i, i+2):
                for k in range(1, 4):
                    nx = x + dx[j] * k
                    ny = y + dy[j] * k
                    
                    # 구역을 벗어나거나 p의 김밥이 아니라면 멈춤
                    if not (0 <= nx < 6 and 0 <= ny < 7) or arr[nx][ny] != p:
                        break
                    cnt += 1
            else:
                # 현재 방향에서 찾는 p의 김밥이 3개 이상이라면, +1(지금 놓은 김밥)까지 합쳐 4개 이상이 됨.
                if cnt >= 3:
                    return p
        return -1


    for i, (s, j) in enumerate(data, start=1):
        # 상근이 먼저
        if check(s, 0) == 0:
            return f"sk {i}"
        
        if check(j, 1) == 1:
            return f"ji {i}"
    
    return "ss"


main()