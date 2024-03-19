def solution(arr1, arr2):
    ret = []
    for i in range(len(arr1)):
        curr = []
        for k in range(len(arr1[0])):
            curr.append(arr1[i][k] + arr2[i][k])
        ret.append(curr)
    return ret

# zip을 사용한 아름다운 코드! pythonic하다.
def sumMatrix(A,B):
    answer = [[c + d for c, d in zip(a,b)] for a, b in zip(A,B)]
    return answer