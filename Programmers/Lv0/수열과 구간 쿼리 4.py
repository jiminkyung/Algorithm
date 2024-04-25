def solution(arr, queries):
    for s, e, k in queries:
        for i in range(s, e+1):
            if k != 0 and i%k == 0:
                arr[i] += 1
    return arr

# 다른사람 답안. k가 0인경우 에러. <- 참고함
def solution(arr, queries):
    for s, e, k in queries:
        for i in range(s, e+1):
            if i%k == 0:
                arr[i] += 1
    return arr