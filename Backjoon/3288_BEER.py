# 구현
# 그리디 알고리즘
# 시뮬레이션


# 문제: https://www.acmicpc.net/problem/3288
# 메모리: 32412KB / 시간: 32ms
from sys import stdin


input = stdin.readline

def main():
    N = int(input())

    # 위(U)부터 시계방향
    dis = {"U": 0, "R": 1, "D": 2, "L": 3}
    arr = [list(map(lambda x: dis[x], input().rstrip())) for _ in range(N)][::-1]

    ret = []

    # 🚨연쇄적으로 회전하는게 아님. 현재 돌린 맥주통 바로 윗줄의 맥주통(왼, 오)만 회전함.
    def turning(x, y):
        # 선택한 맥주통은 시계방향으로, 아래의 따라서 돌아가는 맥주통들은 반시계방향으로 회전시킴.
        arr[x][y] = (arr[x][y] + 1) % 4

        # 왼쪽 위
        if x+1 < N and y-1 >= 0:
            arr[x+1][y-1] = (arr[x+1][y-1] - 1) % 4
        
        # 오른쪽 위
        if x+1 < N and y < len(arr[x+1]):
            arr[x+1][y] = (arr[x+1][y] - 1) % 4


    for i in range(N):
        for j in range(len(arr[i])):
            if arr[i][j] == 0:
                continue

            # 한 번 돌릴때마다 결과값에 추가
            while arr[i][j] != 0:
                turning(i, j)
                ret.append(f"{i+1} {j+1}")

    print(*ret, sep="\n")


main()