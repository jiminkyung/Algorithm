def solution(rsp):
    ret = ""
    for i in rsp:
        if i == "2":
            ret += "0"
        elif i == "0":
            ret += "5"
        else:
            ret += "2"
    return ret

# 우왕 딕셔너리를 이용한 풀이!
def solution(rsp):
    d = {'0':'5','2':'0','5':'2'}
    return ''.join(d[i] for i in rsp)