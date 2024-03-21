def solution(s):
    return int(s)

# 알고리즘적으로 풀어보기...
def solution(s):
    ret = 0
    for i, k in enumerate(s[::-1]):
        if k == "-":
            ret *= (-1)
        elif k == "+":
            break
        else:
            ret += int(k) * 10 ** i
    return ret