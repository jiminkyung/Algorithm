def solution(s):
    ret = sorted(map(int, s.split()))
    return f"{ret[0]} {ret[-1]}"