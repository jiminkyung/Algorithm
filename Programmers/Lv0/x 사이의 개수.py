def solution(myString):
    s = myString.split("x")
    return [len(i) for i in s]