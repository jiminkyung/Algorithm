# 약수, 배수와 소수 2단계
# 메모리: 31120KB / 32ms

from sys import stdin


input = stdin.readline

A, B = map(int, input().split())
a, b = A, B

while b:
    a, b = b, a%b

print(A*B // a)