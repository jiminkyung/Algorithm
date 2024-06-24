# 스택, 큐, 덱
# 메모리: 31120KB / 시간: 48ms

# 반례: https://www.acmicpc.net/board/view/137024

from sys import stdin


input = stdin.readline

N = int(input())
students = list(map(int, input().split()))
passed = []
stack = []

order = 1
i = 0
while i < N:
    if stack and order == stack[-1]:
        passed.append(stack.pop())
        order += 1
        continue

    if students[i] == order:
        order += 1
        passed.append(students[i])
    else:
        stack.append(students[i])
    i += 1

ret = passed + stack[::-1]

print("Nice" if ret == sorted(students) else "Sad")


# 더 효율적으로 리팩토링하기.
# 시간: 32ms
from sys import stdin


input = stdin.readline

N = int(input())
students = list(map(int, input().split()))
stack = []
order = 1

for student in students:
    if student == order:
        order += 1
        while stack and stack[-1] == order:
            stack.pop()
            order += 1
    else:
        stack.append(student)

print("Nice" if not stack else "Sad")