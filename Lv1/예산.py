def solution(d, budget):
    dd = sorted(d)
    ret = [1 for i in range(len(dd)) if sum(dd[:i+1]) <= budget]
    return sum(ret)