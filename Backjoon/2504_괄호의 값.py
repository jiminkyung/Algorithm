# 문제집 - 0x08강 - 스택의 활용(수식의 괄호 쌍)


# 문제: https://www.acmicpc.net/problem/2504

# 아래 블로그를 참고해서 작성했다. 자세한 설명이 기재되어있음.
# 참고👉 https://velog.io/@rhdmstj17/%EB%B0%B1%EC%A4%80-2504%EB%B2%88-%EA%B4%84%ED%98%B8%EC%9D%98-%EA%B0%92-python-stack-%EC%9E%90%EC%84%B8%ED%95%9C-%ED%92%80%EC%9D%B4

# 메모리: 31120KB / 시간: 44ms
from sys import stdin


brackets = stdin.readline().rstrip()
bracket = {"(": 2, "[": 3}
stack = []
ret = 0
tmp = 1

for i, b in enumerate(brackets):
    # 여는괄호라면 tmp에 해당하는 값을 곱해주고 stack에 추가
    if b in bracket:
        tmp *= bracket[b]
        stack.append(b)
    else:  # 닫힌괄호일때
        if b == ")":
            # 괄호쌍이 맞지 않으면 break
            if not stack or stack[-1] == "[":
                ret = 0
                break

            # 한 쌍의 괄호라면 tmp를 ret에 더해주고, 해당 괄호의 짝을 stack에서 pop한다.
            # 그리고 2 or 3으로 나눠준다. 바깥의 괄호들은 아직 닫히지 않은 상태이기 때문.
            if brackets[i-1] == "(":
                ret += tmp
            stack.pop()
            tmp //= 2
        else:
            if not stack or stack[-1] == "(":
                ret = 0
                break

            if brackets[i-1] == "[":
                ret += tmp
            stack.pop()
            tmp //= 3

print(0 if stack else ret)