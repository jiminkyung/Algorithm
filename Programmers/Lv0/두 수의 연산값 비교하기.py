def solution(a, b):
    sum_ab = int(str(a)+str(b))
    return sum_ab if sum_ab == (2*a*b) else max(sum_ab, (2*a*b))