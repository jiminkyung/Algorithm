# 누적 합

# 시간 초과.
from sys import stdin


input = stdin.readline
N, M, K = map(int, input().split())
board = [[1 if c == "B" else 0 for c in input().rstrip()] for _ in range(N)]

def painting():
    dp = [[0]*(M+1) for _ in range(N+1)]

    for i in range(1, N+1):
        for j in range(1, M+1):
            dp[i][j] = board[i-1][j-1] + dp[i][j-1] + dp[i-1][j] - dp[i-1][j-1]
    
    min_change = float("inf")

    for i in range(1, N-K+2):
        for j in range(1, M-K+2):
            change = sum((x+y)%2 != board[i+x-1][j+y-1] for x in range(K) for y in range(K))

            min_change = min(min_change, change, K*K - change)
    
    return min_change

print(painting())


# PyPy3로 제출해서 성공... 애초에 Python3로는 통과할 수 없는 문제였다.
# 참고 1: https://zerotay.tistory.com/257
# 참고 2: https://mgyo.tistory.com/773
from sys import stdin

input = stdin.readline
N, M, K = map(int, input().split())
board = [list(input().rstrip()) for _ in range(N)]

def painting(color):
    dp = [[0]*(M+1) for _ in range(N+1)]
    for i in range(N):
        for j in range(M):
            if (i+j) % 2 == 0:
                value = board[i][j] != color
            else:
                value = board[i][j] == color
            dp[i+1][j+1] = dp[i][j+1] + dp[i+1][j] - dp[i][j] + value

    min_change = float("inf")
    
    for i in range(1, N-K+2):
        for j in range(1, M-K+2):
            count = dp[i+K-1][j+K-1] - dp[i+K-1][j-1] - dp[i-1][j+K-1] + dp[i-1][j-1]
            min_change = min(min_change, count)
    return min_change

print(min(painting("B"), painting("W")))