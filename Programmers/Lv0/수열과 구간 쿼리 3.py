def solution(arr, queries):
    for i in range(len(queries)):
        q1, q2 = queries[i]
        arr[q1], arr[q2] = arr[q2], arr[q1]
    return arr

# 굳이 queries[i]로 안빼줘도 됐었네???
def solution(arr, queries):
    for a,b in queries:
        arr[a],arr[b]=arr[b],arr[a]
    return arr