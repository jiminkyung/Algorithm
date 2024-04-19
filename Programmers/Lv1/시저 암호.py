# 알고리즘 참고 https://seongonion.tistory.com/126

def solution(s, n):
    ret = ""
    for i in s:
        if i.isupper():
            ret += chr(ord("A") + ((ord(i) + n - ord("A")) % 26))
        elif i.islower():
            ret += chr(ord("a") + ((ord(i) + n - ord("a")) % 26))
        else:
            ret += i
    return ret