# 문제집 - BOJ 길라잡이 베타 (1)


# 문제: https://www.acmicpc.net/problem/6588
# 메모리: 46748KB / 시간: 620ms
from sys import stdin


input = stdin.readline

MAX = 1000000
primes = [False, False] + [True]*MAX

for i in range(2, int(MAX**0.5)+1):
    if primes[i]:
        for j in range(i*i, MAX+1, i):
            primes[j] = False

p_nums = [i for i in range(2, MAX+1) if primes[i]]

def is_possible(n):
    for p in p_nums:
        if primes[n-p]:  # if n-p in p_nums는 시간초과.
            print(f"{n} = {p} + {n-p}")
            return
    print("Goldbach's conjecture is wrong.")

while True:
    n = int(input())

    if n == 0:
        break

    is_possible(n)