def solution(n):
    if n % 6 == 0:
        return n // 6

    i = 2
    while True:
        if n * i % 6 == 0:
            return n * i // 6
        i += 1

# 나보다 더 간결한 코드...
def solution(n):
    i=1
    while(1):
        if (6*i)%n==0:
            return i
        i+=1