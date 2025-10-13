# 구현
# 시뮬레이션


# 문제: https://www.acmicpc.net/problem/2578

# 구현 연습하기 좋은 문제!
# 메모리: 32544KB / 시간: 36ms
from sys import stdin


input = stdin.readline

def main():
    arr = [list(map(int, input().split())) for _ in range(5)]
    nums = [tuple(map(int, input().split())) for _ in range(5)]

    # mapping[x]: 숫자 x가 위치한 좌표
    mapping = {arr[i][j]: (i, j) for i in range(5) for j in range(5)}
    bingo = 0  # 전체 빙고 수(지운 줄 수)

    def check(x: int, y: int) -> bool:
        nonlocal bingo

        # 좌/우, 하/상, 우상/좌하, 좌상/우하
        dx = [0, 0, 1, -1, -1, 1, -1, 1]
        dy = [-1, 1, 0, 0, 1, -1, -1, 1]

        # 방향 쌍 확인
        for i in range(0, 8, 2):
            cnt = 0  # 해당 라인에서 발견된 빙고 수
            for j in range(2):
                for k in range(1, 5):
                    nx = x + dx[i+j] * k
                    ny = y + dy[i+j] * k

                    # 범위를 벗어나거나 지운 숫자가 아니라면 break
                    if not (0 <= nx < 5 and 0 <= ny < 5) or arr[nx][ny]:
                        break

                    cnt += 1
            
            # 현재 숫자를 제외하고 모든 칸이 지워졌다면 빙고 +1
            if cnt == 4:
                bingo += 1
        
        return bingo >= 3  # 현재까지 발견한 빙고가 3개 이상이라면 게임 끝


    for i in range(5):
        for j in range(5):
            num = nums[i][j]
            x, y = mapping[num]
            arr[x][y] = 0  # 해당 숫자가 위치한 좌표 값을 0으로 변경(체크)

            if check(x, y):
                print(i * 5 + (j+1))
                return


main()