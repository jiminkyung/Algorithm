def solution(x):
    num = str(x)
    ret = eval("+".join(num))
    return bool(x % ret == 0)