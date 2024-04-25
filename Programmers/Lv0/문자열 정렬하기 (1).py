import re

def solution(my_string):
    s = re.findall(r"\d", my_string)
    return sorted(map(int, s))