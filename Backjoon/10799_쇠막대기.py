# 문제집 - 0x08강 - 스택의 활용(수식의 괄호 쌍)


# 문제: https://www.acmicpc.net/problem/10799
# 메모리: 31552KB / 시간: 64ms
from sys import stdin


brackets = stdin.readline().rstrip()

stack = []
cnt = 0

for i in range(len(brackets)):
    if brackets[i] == "(":
        stack.append(brackets[i])
    else:
        stack.pop()
        if brackets[i-1] == "(":  # 레이저() 라면 스택의 길이(열려있는 막대기의 수)를 더해준다.
            cnt += len(stack)
        else:  # 아니라면 막대의 끝(조각의 끝)을 의미하므로 1만 더해준다.
            cnt += 1

print(cnt)