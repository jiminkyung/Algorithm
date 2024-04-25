def solution(n):
    return sum(filter(lambda x: x % 2 == 0, [i for i in range(1, n+1)]))