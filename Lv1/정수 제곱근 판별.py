def solution(n):
    a = int(n**0.5)
    if a**2 == n:
        return (a+1)**2
    else:
        return -1