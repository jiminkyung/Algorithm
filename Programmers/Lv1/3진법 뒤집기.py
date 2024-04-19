def solution(n):
    s = ""
    while n >= 1:
        s = str(n%3) + s
        n //= 3
    ret = 0
    for i in range(len(s)):
        ret += int(s[i]) * 3 ** i
    return ret