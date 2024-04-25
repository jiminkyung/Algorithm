# 피자좀 그만 나눠먹어라

def solution(n):
    if n % 7 == 0:
        return n // 7
    elif n < 7:
        return 1
    else:
        return n // 7 + 1