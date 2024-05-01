"""
그리디 문제.
enumerate + sort + while + if 로 풀다가 실패.
아래는 제일 효율적인 코드. 스택을 이용한 풀이다.
"""

def solution(number, k):
    stack = []
    
    for num in number:
        # 스택에 값이 있고, 스택의 마지막 값이 현재 숫자보다 작고, k가 0보다 크면
        while stack and stack[-1] < num and k > 0:
            stack.pop()  # 스택에서 값을 제거하고
            k -= 1  # k를 1 감소시킴
        stack.append(num)  # 현재 숫자를 스택에 추가
    
    # 만약 k가 아직 0보다 크다면
    if k > 0:
        stack = stack[:-k]  # 스택의 뒷부분에서 k개의 숫자를 제거
    
    return "".join(stack)  # 스택의 숫자들을 문자열로 합쳐서 반환