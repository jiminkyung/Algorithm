def solution(myString):
    s = myString.split("x")
    return sorted(list(filter(lambda x: x, s)))