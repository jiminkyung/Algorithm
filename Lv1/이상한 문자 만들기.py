def solution(s):
    ret = ""
    x = 0
    for i in range(len(s)):
        if s[i].isalpha():
            if x % 2 == 0:
                ret += s[i].upper()
            else:
                ret += s[i].lower()
            x += 1
        else:
            ret += s[i]
            x = 0
    return ret

# 와우 한줄코드ㅋㅋ
def toWeirdCase(s):
    return " ".join(map(lambda x: "".join([a.lower() if i % 2 else a.upper() for i, a in enumerate(x)]), s.split(" ")))