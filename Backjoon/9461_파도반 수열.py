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