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


# a, b를 n의 절반값으로 지정 후 감소, 증가 시키며 찾는 풀이!
# 40ms로 매우 빠름... 출처: https://www.acmicpc.net/source/83550411
import sys
input = sys.stdin.readline

def initializePrimeNumbers(max_number):
    is_prime = [True] * (max_number + 1)
    is_prime[0] = False
    is_prime[1] = False
    number = 2
    while number * number <= max_number:
        if not is_prime[number]:
            number += 1
            continue
        for i in range(number + number, max_number + 1, number):
            is_prime[i] = False
        number += 1
    return is_prime

def solution(number, is_prime):
    if number == 4:
        return '2 2'
    number1 = number // 2
    number2 = number1
    if number1 % 2 == 0:
        number1 -= 1
        number2 += 1
    while not is_prime[number1] or not is_prime[number2]:
        number1 -= 2
        number2 += 2
    return f'{number1} {number2}'
    

T = int(input())
numbers = list(int(input()) for _ in range(T))
max_number = max(numbers)
is_prime = initializePrimeNumbers(max_number)
answer = []
for number in numbers:
    answer.append(solution(number, is_prime))

print('\n'.join(answer))