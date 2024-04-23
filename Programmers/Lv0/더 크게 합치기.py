def solution(a, b):
    sum_ab = int(str(a)+str(b))
    sum_ba = int(str(b)+str(a))
    return sum_ab if sum_ab == sum_ba else max(sum_ab, sum_ba)