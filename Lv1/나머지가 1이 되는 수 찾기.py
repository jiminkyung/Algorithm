def solution(n):
    n -= 1
    ret = [i for i in range(2, n+1) if not n%i]
    return ret[0]