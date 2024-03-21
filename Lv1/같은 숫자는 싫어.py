def solution(arr):
    ret = [arr[0]]
    for a in arr[1:]:
        if a != ret[-1]:
            ret.append(a)
    return ret

# 인덱싱 에러해결방법! 슬라이싱!!! 다른분의 코드.
def no_continuous(s):
    a = []
    for i in s:
        if a[-1:] == [i]: continue
        a.append(i)
    return a
# 이렇게 a[-1:]로 해버리면 빈 배열이라도 에러가 안난다ㅎㅎㅎ