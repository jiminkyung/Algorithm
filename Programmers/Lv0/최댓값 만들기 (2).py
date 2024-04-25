def solution(numbers):
    n = sorted(numbers)
    ret1 = n[-1] * n[-2]
    ret2 = n[0] * n[1]
    return max(ret1, ret2)