# 누적 합

from sys import stdin


input = stdin.readline
N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

sum_arr = [[0] * (N+1) for _ in range(N+1)]
curr = 0

for i in range(1, N+1):
    for j in range(1, N+1):
        curr += arr[i-1][j-1]
        sum_arr[i][j] = curr

for _ in range(M):
    x1, y1, x2, y2 = map(int, input().split())
    if y2 == 1:
        print(sum_arr[x2][y2] - sum_arr[x1-1][N])
    else:
        print(sum_arr[x2][y2] - sum_arr[x1][y1-1])


# 단순한 구간 합이 아니었음. 사각형 영역의 합을 구해야함.
# 메모리: 105940KB / 시간: 1100ms
from sys import stdin


input = stdin.readline
N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

dp = [[0] * (N+1) for _ in range(N+1)]

for i in range(1, N+1):
    for j in range(1, N+1):
        # (i, j)까지의 누적 합 = 원본배열[i-1][j-1]에 해당하는 값 + 위쪽까지의 합 + 왼쪽까지의 합 - 대각선부분까지의 합(중복제거)
        dp[i][j] = arr[i-1][j-1] + dp[i-1][j] + dp[i][j-1] - dp[i-1][j-1]

for _ in range(M):
    x1, y1, x2, y2 = map(int, input().split())
    # (x2, y2)까지의 누적 합 - 사각형영역의 위쪽 부분 - 사각형영역의 왼쪽 부분 + 대각선부분(중복뺄셈 방지)
    print(dp[x2][y2] - dp[x1-1][y2] - dp[x2][y1-1] + dp[x1-1][y1-1])


# 더 효율적인 코드 발견. 메모리: 73144KB / 시간: 640ms
# tmp: 현재 행의 누적 합
import sys


def solve():
    input = sys.stdin.readline
    print = sys.stdout.write
    n, m = map(int, input().split())
    a = [[0]*(n+1)]
    for _ in range(n):
        a.append([0])
        tmp = 0
        for i, v in enumerate(map(int, input().split()), start=1):
            tmp += v
            a[-1].append(a[-2][i]+tmp)
    for _ in range(m):
        x1, y1, x2, y2 = map(int, input().split())
        x1, y1 = x1-1, y1-1
        print(f'{a[x2][y2]-a[x1][y2]-a[x2][y1]+a[x1][y1]}\n')


solve()