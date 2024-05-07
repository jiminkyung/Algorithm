"""
bracket: 괄호 짝이 담긴 딕셔너리. 닫힌괄호:열린괄호 형태로 키:값을 부여함.
lefted: 왼쪽으로 i칸 이동한 s
is_True: 괄호쌍의 참/거짓을 판별할 변수. 쌍이 맞지 않는 괄호를 발견할 시 False.
passed: 열린괄호들을 담을 리스트
"""

def solution(s):
    bracket = {"}": "{", "]": "[", ")": "("}
    ret = 0
    for i in range(len(s)):
        lefted = s[i:] + s[:i]
        is_True = True
        passed = []
        for l in lefted:
            if l in bracket.values():
                passed.append(l)
                continue

            if passed and bracket[l] == passed[-1]:
                passed.pop()
            else:
                is_True = False
                break

        if is_True and not passed:
            ret += 1
    return ret