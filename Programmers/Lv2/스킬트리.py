"""
ret: 가능한 스킬 수
is_True: 해당 스킬이 skill의 순서조건에 맞는지 판단
tmp: skill을 인덱싱할때 사용할 변수

1. 스킬트리 순회
2. 각 스킬의 요소 순회
3. 만약 해당 요소가 skill에 존재한다면
3.1 skill의 tmp번째 인덱스와 일치할경우(순서가 올바를경우) tmp 값 추가
3.2 아닐경우 is_True를 False로 변경
4. 스킬 요소 순회 후 is_True가 True라면 ret에 1 추가
"""

def solution(skill: str, skill_trees: list) -> int:
    ret = 0

    for skills in skill_trees:
        tmp = 0
        is_True = True

        for s in skills:
            if s in skill:
                if skill[tmp] == s:
                    tmp += 1
                else:
                    is_True = False

        if is_True:
            ret += 1
    return ret