# 문제집 - 0x12강 - 수학


# 문제: https://www.acmicpc.net/problem/9020
# 메모리: 32412KB / 시간: 1260ms
from sys import stdin


input = stdin.readline


primes = [True] * 10001
primes[0] = primes[1] = False

for i in range(2, int(10000**0.5)+1):
    if primes[i]:
        for j in range(i*i, 10001, i):
            primes[j] = False

for _ in range(int(input())):
    n = int(input())
    min_value = 10000
    ret = (0, 0)

    # n의 절반까지만 체크한다. a = n-i 일경우, i + a 나 a + i 나 같이 때문. 자동으로 오름차순이 된다.
    for i in range(2, n//2 + 1):
        if primes[i] and primes[n-i]:
            if abs(i - (n-i)) < min_value:
                ret = (i, n-i)
                min_value = abs(i - (n-i))
    
    print(*ret)