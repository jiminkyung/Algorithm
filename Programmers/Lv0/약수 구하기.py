# 무작정 for문쓰면 그램 터짐
def solution(n):
    root = int(n ** 0.5)
    ret = []
    for i in range(1, root+1):
        if n % i == 0:
            ret.append(i)
            if (n // i) not in ret:
                ret.append(n // i)
    return sorted(ret)