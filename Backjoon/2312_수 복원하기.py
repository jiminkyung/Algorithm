# 문제집 - 0x12강 - 수학


# 문제: https://www.acmicpc.net/problem/2312
# 메모리: 33192KB / 시간: 2124ms
from sys import stdin


input = stdin.readline

primes = [True] * 100001
primes[0] = primes[1] = False

for i in range(2, int(100001 ** 0.5) + 1):
    if primes[i]:
        for j in range(i*i, 100001, i):
            primes[j] = False

for _ in range(int(input())):
    N = int(input())
    numbers = {}

    for i in range(2, 100001):
        if primes[i]:
            while N % i == 0:
                N //= i
                numbers[i] = numbers.get(i, 0) + 1
    
    for k, v in numbers.items():
        print(k, v)