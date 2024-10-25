# 문제집 - BOJ 길라잡이 베타 (1)


# 문제: https://www.acmicpc.net/problem/11727

# 타일 1개를 추가할때 1x2 타일 하나만 가능
# 타일 2개를 추가할때 2x2 타일, 2x1타일*2 가능. 1x2타일*2는 위의 경우와 겹치게 됨.
# 따라서 f(n) = f(n-1) + 2 * (f-2)이 된다.

# 메모리: 31252KB / 시간: 36ms
from sys import stdin


n = int(stdin.readline())
mod = 10007

def fibonacci(n):
    arr = [1] * (n+1)

    if n >= 2:
        arr[2] = 3

        for i in range(3, n+1):
            arr[i] = (arr[i-1] + 2 * arr[i-2]) % mod
    return arr[-1]

print(fibonacci(n))