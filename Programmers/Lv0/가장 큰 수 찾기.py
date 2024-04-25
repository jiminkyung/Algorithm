def solution(array):
    # sorted를 쓰지 말고 풀어보자...
    ret = max(array)
    return [ret, array.index(ret)]