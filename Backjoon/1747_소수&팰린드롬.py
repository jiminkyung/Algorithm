# 문제집 - 대학생 기본반


# 문제: https://www.acmicpc.net/problem/1747
# 메모리: 39712KB / 시간: 196ms
N = int(input())

def check_primes(n):
    primes = [True] * (n+1)
    primes[0] = primes[1] = False

    for i in range(2, int(n ** 0.5) + 1):
        if primes[i]:
            for j in range(i*i, n+1, i):
                primes[j] = False
    return primes

def check_palindrome(n):
    n = str(n)
    if len(n) % 2 == 0:
        if n[:len(n)//2] == n[:len(n)//2 - 1:-1]:
            return True
    else:
        if n[:len(n)//2] == n[:len(n)//2:-1]:
            return True
    return False

# 주어지는 N의 범위가 1000000까지이므로, 그 이상의 답이 나올 수 있도록 만들어놔야한다.
primes = check_primes(1100000)

while True:
    if primes[N] and check_palindrome(N):
        print(N)
        break
    N += 1