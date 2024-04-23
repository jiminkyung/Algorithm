def solution(n):
    if n % 2 != 0:
        return sum(i for i in range(1, n+1, 2))
    else:
        return sum(i*i for i in range(2, n+1, 2))