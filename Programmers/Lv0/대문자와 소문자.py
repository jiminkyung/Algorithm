def solution(my_string):
    ret = ''
    for i in my_string:
        if i.isupper():
            ret += i.lower()
        else:
            ret += i.upper()
    return ret

# 개사기 코드 ㅋㅋ 와우 이런게 있었구나
def solution(my_string):
    return my_string.swapcase()