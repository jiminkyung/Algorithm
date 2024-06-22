# 약수, 배수와 소수 2단계
# 메모리: 33048KB / 시간: 276ms


# 에라토스테네스의 체를 이용한 풀이.
from sys import stdin


input = stdin.readline

_max = 123456*2  # 체크범위가 n부터 2n까지이므로 max(123,456)의 두배만큼 만들어둬야함.
primes = [True] * (_max+1)
primes[0] = primes[1] = False

for i in range(2, int(_max**0.5)+1):
    if primes[i]:
        for j in range(i*i, _max+1, i):
            primes[j] = False

def check_primes(num):
    cnt = 0
    for i in range(num+1, 2*num+1):
        if primes[i]:
            cnt += 1
    return cnt

while True:
    n = int(input())
    if not n:
        break
    print(check_primes(n))