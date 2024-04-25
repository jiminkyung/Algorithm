def solution(myString):
    ret = ""

    for alp in myString:
        if ord(alp) < ord("l"):
            ret += "l"
        else:
            ret += alp
    return ret

# ord 안써도 됨