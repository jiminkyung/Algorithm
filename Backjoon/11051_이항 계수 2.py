# 문제집 - 0x12강 - 수학


# 문제: https://www.acmicpc.net/problem/11051

# ⭐ 11401_이항 계수 3 문제와 동일하다.
# 모듈러 연산, 페르마의 소정리 개념을 활용해야한다.

# 메모리: 32544KB / 시간: 40ms
from sys import stdin


input = stdin.readline
MOD = 10007

N, K = map(int, input().split())

def factorial(n):
    fact = 1
    for i in range(2, n+1):
        fact = (fact * i) % MOD
    return fact


def square(n, k):
    if k == 0:
        return 1
    
    tmp = square(n, k//2)

    if k % 2 == 0:
        return (tmp * tmp) % MOD
    else:
        return (tmp * tmp * n) % MOD

# 이항계수 공식👉 N! / K!(N-K)!
top = factorial(N)
bottom = factorial(N-K) * factorial(K)

print(top * square(bottom, MOD-2) % MOD)