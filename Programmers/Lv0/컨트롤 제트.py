def solution(s):
    lst = s.split()
    ret = []
    for i in lst:
        if i == "Z":
            ret.pop()
        else:
            ret.append(int(i))
    return sum(ret)