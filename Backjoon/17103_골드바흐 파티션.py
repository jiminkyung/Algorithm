# 약수, 배수와 소수 2단계
# 메모리: 42520KB / 시간: 2092ms

from sys import stdin


input = stdin.readline

def make_primes(limit) -> list:
    primes = [True] * (limit+1)
    primes[0] = primes[1] = False

    for i in range(2, int(limit**0.5)+1):
        if primes[i]:
            for j in range(i*i, limit+1, i):
                primes[j] = False
    return primes

primes = make_primes(1000000)

def check_primes(number):
    """
    골드바흐 파티션에 해당하는 수들을 체크하는 함수.
    i와 number-i가 소수이며 checked에 없는 경우 cnt를 1 증가시킨다.
    """
    checked = set()
    cnt = 0
    for i in range(2, number-1):
        if primes[i] and primes[number-i]:
            if i not in checked:
                checked.add(i)
                checked.add(number-i)
                cnt += 1
    return cnt

T = int(input())
for _ in range(T):
    print(check_primes(int(input())))


# 반으로 쪼개면 더 빨라질듯하다.
# 시간: 1096ms
from sys import stdin


input = stdin.readline

def make_primes(limit) -> list:
    primes = [True] * (limit+1)
    primes[0] = primes[1] = False

    for i in range(2, int(limit**0.5)+1):
        if primes[i]:
            for j in range(i*i, limit+1, i):
                primes[j] = False
    return primes

primes = make_primes(1000000)

def check_primes(number):
    """
    checked를 없애는 대신 주어진 수의 절반만큼만 체크하기.
    어차피 i와 number-i 모두 체크하기때문에 실질적인 체크 범위는 같다.
    하지만 코드상의 범위는 수의 절반까지이므로 중복위험은 없음.
    """
    cnt = 0
    for i in range(2, number//2 + 1):
        if primes[i] and primes[number-i]:
                cnt += 1
    return cnt

T = int(input())
for _ in range(T):
    print(check_primes(int(input())))