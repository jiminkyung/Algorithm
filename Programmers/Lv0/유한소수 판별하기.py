# 다른 사람 풀이. gcd함수를 처음 봤다.
from math import gcd

def solution(a, b):
    b = b / gcd(a, b)
    for i in [2, 5]:
        while not b % i:
            b //= i

    return 1 if b == 1 else 2

# 다른 풀이 2
def solution(a, b):
    answer = 0
    for i in range(2, min([a, b]) + 1):
        while a % i == 0 and b % i == 0:
            a = a // i
            b = b // i
    while b % 2 == 0:
        b = b // 2
    while b % 5 == 0:
        b = b // 5
    if b == 1:
        answer = 1
    else:
        answer = 2
    return answer