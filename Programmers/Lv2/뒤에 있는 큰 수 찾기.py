# 문제: https://school.programmers.co.kr/learn/courses/30/lessons/154539

def solution(numbers):
    # 스택에는 각 수의 인덱스를 저장.
    # 현재 수가 top 인덱스의 수보다 크다면, 해당 top 인덱스의 ret 값을 현재 수로 갱신.
    # 아니라면 스택에 현재 수의 인덱스를 추가.
    stack = []
    ret = [-1] * len(numbers)
    
    for i, num in enumerate(numbers):
        while stack and numbers[stack[-1]] < num:
            idx = stack.pop()
            ret[idx] = num
        stack.append(i)
    return ret