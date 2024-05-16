"""
스택 문제.
"""

def solution(order: list) -> int:
    stack = []  # 보조 컨테이너 벨트 역할을 할 스택
    current = 1  # 현재 트럭에 실어야 할 상자 번호
    count = 0  # 트럭에 실은 상자의 수
    
    for box in order:
        while current <= box:
            stack.append(current)
            current += 1
        if stack[-1] == box:
            stack.pop()
            count += 1
        else:
            break

    return count