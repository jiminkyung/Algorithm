def solution(strArr):
    for i in range(len(strArr)):
        if i % 2 != 0:
            strArr[i] = strArr[i].upper()
        else:
            strArr[i] = strArr[i].lower()
    return strArr

# enumerate를 사용하는것을 권장한다고 함.
def solution(strArr):
    for i, s in enumerate(strArr):
        if i % 2 == 0:
            strArr[i] = strArr[i].lower()
        else:
            strArr[i] = strArr[i].upper()
    return strArr
# 시간복잡도가 줄어든다.