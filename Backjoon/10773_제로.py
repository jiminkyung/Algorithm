# 스택, 큐, 덱
# 메모리: 31900KB / 시간: 116ms

# 정수가 0일 경우에 지울 수 있는 수가 있음을 보장.
from sys import stdin


input = stdin.readline

K = int(input())
stack = []

for _ in range(K):
    num = int(input())

    if not num:
        stack.pop()
        continue

    stack.append(num)

print(sum(stack))