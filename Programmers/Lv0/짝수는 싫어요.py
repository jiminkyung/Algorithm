def solution(n):
    return sorted(filter(lambda x: x % 2 != 0, [i for i in range(n+1)]))