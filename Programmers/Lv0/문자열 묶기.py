# 원래 내 코드. 시간복잡도에서 걸림.
# length.count(i) 부분에서 많이 잡아먹는다.

def solution(strArr):
    l = sorted(strArr, key=lambda x: len(x))
    length = []
    for i in strArr:
        length.append(len(i))
    ret = {i:length.count(i) for i in length}
    return max(ret.values())

# AI teacher에게 re-coding을 맡긴 결과ㅎㅎ
def solution(strArr):
    length_dict = {}

    for string in strArr:
        length = len(string)
        if length in length_dict:
            length_dict[length] += 1
        else:
            length_dict[length] = 1

    return max(length_dict.values())

# 위의 AI버전 내 코드에서 더 간략해진 코드.
def solution(strArr):
    d = {}

    for i in strArr:
        d[len(i)] = d.get(len(i), 0) + 1

    return max(d.values())

# 복세편살 코드
def solution(strArr):
    a=[0]*31
    for x in strArr: a[len(x)]+=1
    return max(a)
# 조건에 '1 ≤ strArr의 원소의 길이 ≤ 30'가 있었다.
# 즉 나올 수 있는 길이는 1부터 30까지.
# 하지만 인덱스는 0부터 시작하므로 31개로 만들어줌.