# 분할 정복

"""
A를 B번 곱한 값을 C로 나눈 나머지값...
이걸 0.5초만에 해결해보려면, 어떻게 분할??

2^8 = 2^4 * 2^4
2^4 = 2^2 * 2^2
2^2 = ... 이렇게?
근데 B가 홀수라면?
2^9 = 2^4 * 2^4 * 2
"""

# 메모리: 31120KB / 시간: 32ms

A, B, C = map(int, input().split())

def square(a, b, c):
    if b == 0:
        return 1
    
    half = square(a, b//2, c)

    if b % 2 == 0:
        return (half * half) % c
    else:
        return (half * half * a) % c

print(square(A, B, C))