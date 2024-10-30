# 문제집 - 0x05강 - 스택


# 문제: https://www.acmicpc.net/problem/2493
# 메모리: 130844KB / 시간: 632ms
from sys import stdin


input = stdin.readline

N = int(input())
top = list(map(int, input().split()))

stack = []
ret = [0] * N

for i in range(N):
    while stack:
        if stack[-1][1] > top[i]:
            ret[i] = stack[-1][0] + 1
            break
        stack.pop()
    stack.append((i, top[i]))

print(*ret)