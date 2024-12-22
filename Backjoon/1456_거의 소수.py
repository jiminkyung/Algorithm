# 문제집 - 0x12강 - 수학


# 문제: https://www.acmicpc.net/problem/1456

# 에라토스테네스의 체 문제
# 메모리: 110536KB / 시간: 3384ms
from sys import stdin


input = stdin.readline

A, B = map(int, input().split())
# 어차피 어떤 수 i가 소수일때, i*i는 B보다 같거나 작아야하므로 "소수 판정"은 B의 제곱근까지만 진행하면 된다.
root = int(B ** 0.5)

primes = [True] * (root + 1)
primes[0] = primes[1] = False
almost_prime = 0

for i in range(2, root + 1):
    if primes[i]:
        for j in range(i*i, root + 1, i):
            primes[j] = False
        x = i*i
        while x <= B:
            if x >= A:
                almost_prime += 1
            x *= i

print(almost_prime)