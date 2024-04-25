def solution(arr, queries):
    result = []
    for s, e, k in queries:
        lst = list(filter(lambda x: x>k, arr[s:e+1]))
        result.append(min(lst)) if lst else result.append(-1)
    return result