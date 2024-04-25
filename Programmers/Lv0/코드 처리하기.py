def solution(code):
    mode = 0
    ret = ''
    for idx in range(len(code)):
        if mode == 0:
            if code[idx] != "1" and idx % 2 == 0:
                ret += code[idx]
            elif code[idx] == "1":
                mode = 1
        else:
            if code[idx] != "1" and idx % 2 != 0:
                ret += code[idx]
            elif code[idx] == "1":
                mode = 0
    return ret if ret else "EMPTY"

# 미친듯이 간결하다. 변태코딩.
def solution(code):
    return "".join(code.split("1"))[::2] or "EMPTY"

# 더 직관적이다.
def solution(code):
    answer = ''

    mode = 0
    for i in range(len(code)):
        if code[i] == '1':
            mode ^= 1
        else:
            if i % 2 == mode:
                answer += code[i]

    return answer if answer else 'EMPTY'