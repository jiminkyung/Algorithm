def solution(quiz):
    ret = []
    for i in quiz:
        q, s = i.split("=")
        if eval(q) == int(s):
            ret.append("O")
        else:
            ret.append("X")
    return ret