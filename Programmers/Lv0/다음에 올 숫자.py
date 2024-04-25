def solution(common):
    dif = common[1] - common[0]
    if common[2] - common[1] != dif:
        x = common[1] // common[0]
        return common[-1] * x
    else:
        return common[-1] + dif