def solution(array, commands):
    ret = []
    for i, j, k in commands:
        arr = sorted(array[i-1:j])
        ret.append(arr[k-1])
    return ret