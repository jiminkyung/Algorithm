# 문제집 - 0x12강 - 수학


# 문제: https://www.acmicpc.net/problem/5347
# 메모리: 32412KB / 시간: 32ms
from sys import stdin


input = stdin.readline

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


for _ in range(int(input())):
    a, b = map(int, input().split())
    g = gcd(a, b)
    ret = a * b // g
    print(ret)