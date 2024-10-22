# 문제집 - BOJ 길라잡이 베타 (1)


# 문제: https://www.acmicpc.net/problem/15711
# 메모리: 62372KB / 시간: 4896ms

"""
❌ 두 합이 4보다 작다면 -> a, b중 하나는 1이어야하므로 소수끼리의 합이 될 수 없음.
⭕ 두 합이 2로 나누어 떨어진다면 -> 2를 제외한 짝수는 두 소수의 합으로 나타낼 수 있음(골드바흐의 추측)
만약 둘 다 아닐때,
(합-2)이 MAX보다 크고 MAX범위 내의 소수로 나누어떨어진다면 ❌
(합-2)이 MAX보다 작고 MAX범위 내의 소수라면 ⭕
"""
from sys import stdin


input = stdin.readline

MAX = 2 * (10**6)
primes = [False, False] + [True]*MAX

for i in range(2, int(MAX**0.5)+1):
    if primes[i]:
        for j in range(i*i, MAX+1, i):
            primes[j] = False

p_nums = [i for i in range(2, MAX+1) if primes[i]]

def is_possible(num):
    if num >= MAX:
        for p in p_nums:
            if num % p == 0:
                return False
    else:
        if num not in p_nums:
            return False
    return True

for _ in range(int(input())):
    total = sum(map(int, input().split()))

    if total < 4:
        print("NO")
    elif total % 2 == 0:
        print("YES")
    else:
        print("YES" if is_possible(total-2) else "NO")


# 밀러-라빈 소수 판별법을 사용한 코드! 실행시간 48ms다. 엄청나게 차이난다...
# 밀러-라빈 개념은 공부해봐야할 듯 하다.
# 출처👉 https://www.acmicpc.net/source/53529041
import sys
input = sys.stdin.readline

primes = (2, 7, 61)

def isprime(n):
    if n == 1: return False
    d, s = n - 1, 0
    while d % 2 == 0: d //= 2; s += 1
    for a in primes:
        #if a >= n: break
        P = False
        v = pow(a, d, n)
        if v == 1: P = True; continue
        for r in range(s):
            if v == n-1:
                P = True
                break
            v = pow(v, 2, n)
        if P == False: return False
    return True

T = int(input())
for _ in range(T):
    A, B = map(int, input().split())
    N = A + B
    if N < 4: print("NO")
    elif not N & 1: print("YES")
    elif isprime(N - 2): print("YES")
    else: print("NO")