def solution(arr):
    idx = arr.index(min(arr))
    arr.pop(idx)
    return arr if arr else [-1]