def solution(arr):
    p = -1
    if 2 in arr:
        p = arr.index(2)
    else:
        return [-1]

    for i in range(len(arr)):
        if arr[i] == 2:
            curr = i
    return arr[p:curr+1]

# 간결한 코드...!
# 신박한 방법이다;; 뒤집으면 되는구나
def solution(arr):
    if 2 not in arr:
        return [-1]
    return arr[arr.index(2) : len(arr) - arr[::-1].index(2)]