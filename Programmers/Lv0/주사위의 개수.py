def solution(box, n):
    s = [i // n for i in box]
    return s[0] * s[1] * s[2]