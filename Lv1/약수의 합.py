def solution(n):
    if n == 0:
        return 0

    ret = [1, n]
    x = int(n**0.5)
    for i in range(2, x+1):
        if n % i == 0:
            ret.append(i)
            ret.append(n // i)
    return sum(set(ret))