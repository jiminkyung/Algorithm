# 풀긴 풀었지만 효율이 엄청나게 떨어진다.
def solution(left, right):
    ret = 0
    for i in range(left, right+1):
        curr = 0
        for k in range(1, i+1):
            if i % k == 0:
                curr += 1
        if curr % 2 == 0:
            ret += i
        else:
            ret -= i
    return ret

# 제곱근 개념을 이용한 깔끔한 풀이
def solution(left, right):
    answer = 0
    for i in range(left,right+1):
        if int(i**0.5)==i**0.5:
            answer -= i
        else:
            answer += i
    return answer