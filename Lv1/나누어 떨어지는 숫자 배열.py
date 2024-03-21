def solution(arr, divisor):
    ret = sorted(filter(lambda x: x % divisor == 0, arr))
    return ret if ret else [-1]