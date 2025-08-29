# 구현
# 시뮬레이션


# 문제: https://www.acmicpc.net/problem/2072
# 메모리: 32412KB / 시간: 36ms
from sys import stdin


input = stdin.readline

def main():
    N = int(input())
    field = [[-1] * 19 for _ in range(19)]
    # 바둑돌 좌표를 0-based로 변환해서 저장 
    stones = [tuple(map(lambda x: int(x)-1, input().split())) for _ in range(N)]

    def check(x: int, y: int, color: int) -> bool:
        # 상하, 좌우, \대각선, /대각선
        dx = [-1, 1, 0, 0, -1, 1, -1, 1]
        dy = [0, 0, -1, 1, -1, 1, 1, -1]

        # 8방향을 두개씩 묶어서 탐색
        # 양 방향을 탐색 후 해당 바둑돌이 정확히 5개 이어져있는지 체크
        for i in range(0, 8, 2):
            d = i
            cnt = 0

            for _ in range(2):
                nx, ny = x, y
                for _ in range(19):  # 이어져 있는 바둑돌이 5개 이상일수도 있으므로, 범위를 최댓값으로 설정
                    nx += dx[d]
                    ny += dy[d]

                    # 바둑판 범위를 벗어났거나 돌 색깔이 다르다면 break, 반대 방향으로 넘어감
                    if not (0 <= nx < 19 and 0 <= ny < 19) or field[nx][ny] != color:
                        break

                    cnt += 1
                
                d += 1
            
            # 갯수가 정확히 5개일때만 True 반환
            if cnt + 1 == 5:
                return True
        return False


    color = 0

    for turn, (x, y) in enumerate(stones, start=1):
        field[x][y] = color

        if check(x, y, color):
            print(turn)
            break

        # 턴마다 바둑돌 색상 토글
        color ^= 1
    else:
        print(-1)


main()