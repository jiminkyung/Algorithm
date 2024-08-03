# 스택 2

# 메모리: 42300KB / 시간: 696ms

from sys import stdin


input = stdin.readline

words = input().rstrip()
bomb = input().rstrip()

stack = []
l = len(bomb)

for i in range(len(words)):
    stack.append(words[i])

    if "".join(stack[-l:]) == bomb:  # 만약 stack[-폭발문자열길이:]가 폭발문자열과 같다면,
        for _ in range(l):           # 폭발문자열길이 만큼 pop
            stack.pop()

print("".join(stack) if stack else "FRULA")