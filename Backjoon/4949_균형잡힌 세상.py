# 스택, 큐, 덱
# 메모리: 31120KB / 시간: 72ms

from sys import stdin


input = stdin.readline

brackets = {"(": ")", "[": "]"}

def check_balanced(string) -> bool:
    stack = []

    for s in string:
        if s in brackets:
            stack.append(s)
        elif s in brackets.values():
            if not stack:
                return False
            
            p = stack.pop()
            if brackets[p] != s:
                return False
    return bool(not stack)

while True:
    # 공백없이 온점(.)만 주어졌을때에 while문을 탈출해야 함. => stdin.readline 사용으로 개행문자(\n)까지 포함됨. => 탈출못함.
    # rstrip()으로 개행문자만 없애주는 방법이 있었음. => 탈출 성공.
    sentence = input().rstrip()

    if sentence == ".":
        break

    print("yes" if check_balanced(sentence) else "no")


# 좀 더 깔끔하게...
# 시간: 60ms
from sys import stdin


brackets = {")": "(", "]": "["}

def is_balanced(s):
    stack = []
    for char in s:
        if char in "([":
            stack.append(char)
        elif char in ")]":
            if not stack or stack.pop() != brackets[char]:
                return False
    return not stack

# stdin을 for문에 그대로 사용할 수 있음!
for line in stdin:
    line = line.rstrip()
    if line.rstrip() == ".":
        break
    print("yes" if is_balanced(line) else "no")