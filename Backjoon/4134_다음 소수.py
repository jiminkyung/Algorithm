# 약수, 배수와 소수 2단계


# 첫번째 코드.
# 메모리: 31120KB / 시간: 1468ms
from sys import stdin


input = stdin.readline

def is_prime(number):
    if number in (0, 1):
        return False
    elif number == 2:
        return True
    else:
        for i in range(2, int(number**0.5)+1):
            if number % i == 0:
                return False
    return True

n = int(input())

for _ in range(n):
    num = int(input())

    while True:
        if is_prime(num):
            print(num)
            break
        num += 1


# 두번째 코드. 에라토스테네스의 체를 이용했으나 메모리 초과...
# -> 문제 요구대로 제곱근을 이용하는게 맞는 방법인가보다.
from sys import stdin


input = stdin.readline

def check_prime(limit) -> bool:
    primes = [True] * (limit+1)
    primes[0] = primes[1] = False

    for i in range(2, int(limit**0.5)+1):
        if primes[i]:
            for j in range(i*i, limit+1, i):
                primes[j] = False
    return primes

_max = 4 * 10**9
is_prime = check_prime(_max)

def find_prime(number) -> int:
    while not is_prime[number]:
        number += 1
    return number

n = int(input())

for _ in range(n):
    num = int(input())
    print(find_prime(num))