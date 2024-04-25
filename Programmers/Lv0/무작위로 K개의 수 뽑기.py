def solution(arr, k):
    result = []
    for i in arr:
        if i not in result:
            result.append(i)

    if len(result) >= k:
        return result[:k]
    else:
        return result + [-1]*(k - len(result))

# 좀 더 간결한 버전. 다른분 코드.
def solution(arr, k):
    ret = []
    for i in arr:
        if i not in ret:
            ret.append(i)
        if len(ret) == k:
            break

    return ret + [-1] * (k - len(ret))