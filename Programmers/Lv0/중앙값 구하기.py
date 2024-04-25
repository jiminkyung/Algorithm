def solution(array):
    ret = sorted(array)
    return ret[(len(ret)-1)//2]