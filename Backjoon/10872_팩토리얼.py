# 조합론
# 메모리: 31120KB / 시간: 40ms

def factorial(n):  # 팩토리얼 재귀 함수
    if n <= 1:
        return 1
    return n * factorial(n-1)

print(factorial(int(input())))