def solution(sides):
    x = sorted(sides)
    return 1 if sum(x[:2]) > x[2] else 2