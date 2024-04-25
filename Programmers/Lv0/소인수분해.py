def solution(n):
    num = int(n ** 0.5)
    ret = set()
    i = 2
    while i <= num:
        if n % i == 0:
            ret.add(i)
            n = n // i
        else:
            i += 1
    if n > 1:
        ret.add(n)
    return sorted(ret)