def solution(my_string):
    모음 = ["a", "e", "i", "o", "u"]
    ret = ""
    for i in my_string:
        if i not in 모음:
            ret += i
    return ret