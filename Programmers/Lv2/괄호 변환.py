"""
중간에 AI에게 물어본 문제. 카카오 블라인드 채용 문제 중 하나다.
"""

def is_correct(s):
    """
    올바른 괄호 문자열인지 확인하는 함수.
    stack이 비어있으면 True, 아니면 False 반환.
    """
    stack = []
    for char in s:
        if char == "(":
            stack.append(char)
        else:
            if not stack:
                return False
            stack.pop()
    return not stack # 자동으로 True/False 반환해줌. Pythonic!

def solution(p):
    # 빈 문자열일 경우 "" 반환
    if not p:
        return ""
    
    # w -> u, v 분리
    count = 0
    for i in range(len(p)):
        if p[i] == "(":
            count += 1
        else:
            count -= 1
        if count == 0:
            u = p[:i+1]
            v = p[i+1:]
            break
    
    if is_correct(u):
        return u + solution(v)
    else:
        result = "("
        result += solution(v)
        result += ")"
        u = u[1:-1]
        u = "".join(")" if char == "(" else "(" for char in u)
        result += u
        return result