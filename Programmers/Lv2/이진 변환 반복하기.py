"""
del_zeros: 삭제한 0의 갯수
times: 변환 횟수
length: 각 턴에서 0을 제거한 후의 길이
"""

def solution(s: str) -> list:
    del_zeros = times = length = 0

    while s != "1":
        length = len(s.replace("0", ""))
        del_zeros += len(s) - length
        s = bin(length)[2:]
        times +=1
    return [times, del_zeros]