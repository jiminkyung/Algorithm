# 그리디 알고리즘


# 문제: https://www.acmicpc.net/problem/1455
# 메모리: 32412KB / 시간: 64ms
from sys import stdin


input = stdin.readline

def main():
    N, M = map(int, input().split())
    # "01" -> [0, 1] 변환
    arr = [list(map(int, input().rstrip())) for _ in range(N)]

    cnt = 0

    # (a, b)를 뒤집을경우 (0~a, 0~b)를 뒤집어야 함.
    # => (0, 0)부터 체크하면 (i, j)를 체크하고 뒤집은 후, (i+x, j+x)를 체크할 때 또 뒤집어야 함.
    # => 따라서 끝부터 거꾸로 체크해야 체크 후 상태를 유지 가능.
    for i in range(N-1, -1, -1):
        for j in range(M-1, -1, -1):
            if arr[i][j] == 1:
                cnt += 1
                for r in range(i+1):
                    for c in range(j+1):
                        arr[r][c] ^= 1
    
    print(cnt)


main()