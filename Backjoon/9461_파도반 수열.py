# 동적 계획법 1
# 메모리: 32140KB / 시간: 36ms

import sys


data = iter(map(int, sys.stdin.read().split()))
next(data)

dp = [0, 1, 1]

def padoban(n):
    for _ in range(3, n+1):
        dp.append(dp[-2] + dp[-3])
    return dp[n]

for number in data:
    sys.stdout.write(f"{padoban(number)}\n")


"""
1= 1
2= 1
3= 1
4= 2
5= 2
6= 3
7= 4
8= 5
9= 7
10= 9
11= 12
=> F(N) = F(N-2) + F(N-3)
"""


# 실행시간 더 줄여보기...
# 메모리: 31120KB / 시간: 36ms
import sys


N = int(sys.stdin.readline())

dp = [0, 1, 1, 1, 2] + [0]*96

for i in range(5, 101):
    dp[i] = dp[i-2] + dp[i-3]

for _ in range(N):
    n = int(sys.stdin.readline())
    sys.stdout.write(f"{dp[n]}\n")


# 실행시간 32 찍을때까지.
# 메모리: 31120KB / 시간: 32ms
from sys import stdin


input = stdin.readline
N = int(input())

dp = [0, 1, 1, 1, 2] + [0]*96

for i in range(5, 101):
    dp[i] = dp[i-2] + dp[i-3]

for _ in range(N):
    n = int(input())
    print(dp[n])

# 메모리, 실행시간 차이?
    # => 입/출력처리가 원인일 수 있음.
    # input = stdin.readline 으로 할당하고, stdout 대신 print()를 사용하는게 더 빠를 수도 있다.