def solution(n):
    num = list(str(n))
    return int("".join(sorted(num, reverse=True)))