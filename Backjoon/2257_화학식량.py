# 자료 구조
# 문자열
# 스택


# 문제: https://www.acmicpc.net/problem/2257

# 스택 활용 문제다. 나중에 스택 연습용으로 다시 풀어볼만한 문제.
# 메모리: 32412KB / 시간: 36ms
from sys import stdin


input = stdin.readline

def main():
    weight = {"H": 1, "C": 12, "O": 16}

    data = input().rstrip()
    L = len(data)
    stack = [0]
    
    i = 0

    while i < L:
        # 1. 원자 기호일경우
        if data[i].isalpha():
            curr = weight[data[i]]
            # 이 뒤에 숫자가 붙는지 확인. 숫자가 붙으면 연산 후 포인터를 한 칸 이동시켜준다.
            if i+1 < L and data[i+1].isdigit():
                curr *= int(data[i+1])
                i += 1
            # 숫자 유무와 상관없이 스택의 마지막값에 더해줌
            stack[-1] += curr
        # 2. 여는 괄호 ( 일경우
        elif data[i] == "(":
            # 스택에 새로운 시작값(0)을 추가
            stack.append(0)
        # 3. 닫는 괄호 ) 일경우
        elif data[i] == ")":
            # 마지막 값을 꺼냄
            prev = stack.pop()
            # 바로 뒤에 숫자가 붙는다면 연산 후 포인터 이동.
            if i+1 < L and data[i+1].isdigit():
                prev *= int(data[i+1])
                i += 1
            # 숫자 유무와 상관없이 스택의 마지막값에 더해줌
            stack[-1] += prev
        
        # data[i]가 숫자일 경우는 없음. 1, 3번 케이스에서 다음 문자가 숫자인지 체크하기 때문.
        i += 1
    
    print(stack[0])


main()