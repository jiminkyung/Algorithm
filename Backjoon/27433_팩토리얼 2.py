# 재귀
# 메모리: 31120KB / 시간: 32ms

def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n-1)

print(factorial(int(input())))