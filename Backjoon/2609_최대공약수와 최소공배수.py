# 문제집 - BOJ 길라잡이 베타 (1)


# 문제: https://www.acmicpc.net/problem/2609
# 메모리: 31120KB / 시간: 40ms
from sys import stdin


def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

a, b = map(int, stdin.readline().split())

m = gcd(a, b)
print(m, a * b // m, sep="\n")