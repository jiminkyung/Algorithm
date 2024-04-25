import re

def solution(my_string):
    s = re.sub(r"[^0-9]", " ", my_string)
    ret = s.split()
    return sum(int(i) for i in ret)

# eval("+".join(ret))하면 런타임 에러난다 ^^