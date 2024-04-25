def solution(arr, intervals):
    result = []
    for a, b in intervals:
        result.extend(arr[a:b+1])
    return result