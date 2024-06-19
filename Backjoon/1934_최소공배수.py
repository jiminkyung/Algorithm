# 약수, 배수와 소수 2단계
# 메모리: 31120KB / 시간: 36ms

from sys import stdin


input = stdin.readline

T = int(input())

def gcd(a, b):
    while b:
        a, b = b, a%b
    return a

for _ in range(T):
    A, B = map(int, input().split())
    print(A*B // gcd(A, B))