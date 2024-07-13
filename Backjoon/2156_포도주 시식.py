# 동적 계획법 1

"""
"2579_계단 오르기" 와는 다른 문제다.
현재 와인잔을 선택하지 않을 경우도 고려해야한다.
즉, 체크해야 할 조건은,
- dp[i-1]: 현재 와인을 마시지 않을 경우.
- dp[i-2]+wines[i]: 이 와인만 마시는 경우. 전전 와인+현재 와인.
- dp[i-3]+wines[i-1]+wines[i]: 이 와인과 바로 전 와인을 마시는 경우. 현재 와인+전 와인+전전전 와인까지의 최댓값.
dp[i-4]이상은 고려하지 않음. => dp[i-1~...] 과정에서 포함하고 있음.
"""

# 메모리: 31120KB / 시간: 44ms
from sys import stdin


input = stdin.readline
N = int(input())
wines = [int(input()) for _ in range(N)]

def drunken_with_wines(n):
    if n <= 2:
        return sum(wines)
    
    dp = [0] * N

    dp[0] = wines[0]
    dp[1] = wines[0] + wines[1]
    dp[2] = max(wines[0]+wines[2], wines[1]+wines[2], dp[1])

    for i in range(3, N):
        dp[i] = max(dp[i-1], dp[i-2]+wines[i], dp[i-3]+wines[i-1]+wines[i])
    
    return dp[-1]

print(drunken_with_wines(N))