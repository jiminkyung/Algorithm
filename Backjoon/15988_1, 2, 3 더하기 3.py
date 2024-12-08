# 문제집 - 0x10강 - 다이나믹 프로그래밍


# 문제: https://www.acmicpc.net/problem/15988
"""
1 = 1
2 = 2, 1+1
3 = 3, 2+1, 1+2, 1+1+1
4 = 3+1, 1+3, 2+2, 2+1+1, 1+2+1, 1+1+2, 1+1+1+1
"""
# 메모리: 71968KB / 시간: 448ms
from sys import stdin


input = stdin.readline
MOD = 1000000009

dp = [0] * 1000000
dp[0] = 1
dp[1] = 2
dp[2] = 4

for i in range(3, 1000000):
    dp[i] = (dp[i-1] + dp[i-2] + dp[i-3]) % MOD

for _ in range(int(input())):
    n = int(input())
    print(dp[n-1])


# 행렬을 이용한 훨씬 빠른 풀이...
# 출처👉 https://www.acmicpc.net/source/72849924
import sys
input = sys.stdin.readline
MOD = 1000000009

def mul(a, b):
    r = len(a)
    c = len(b[0])
    s = len(b)

    res = [[0]*c for _ in range(r)]
    for i in range(r):
        for j in range(c):
            for k in range(s):
                res[i][j] += a[i][k] * b[k][j]
                res[i][j] %= MOD

    return res

def eye(n):
    res = [[0]*n for _ in range(n)]
    for i in range(n):
        res[i][i] = 1
    return res

def power(m, p):
    if p == 0:
        n = len(m)
        return eye(n)
    
    elif p == 1:
        return m
    
    x = power(m, p//2)
    x = mul(x, x)

    if p % 2 == 0:
        return x
    else:
        return mul(m, x)

m = [[1, 1, 1], [1, 0, 0], [0, 1, 0]]
x = [[4], [2], [1]]

T = int(input())
for _ in range(T):
    N = int(input())
    print(*mul(power(m, N-1), x)[-1])