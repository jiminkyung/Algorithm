# 문제집 - 0x05강 - 스택


# 문제: https://www.acmicpc.net/problem/6198
# 아직도 어려운 스택...
# 참고👉 https://velog.io/@thguss/%EB%B0%B1%EC%A4%80-6198.-%EC%98%A5%EC%83%81-%EC%A0%95%EC%9B%90-%EA%BE%B8%EB%AF%B8%EA%B8%B0-with.-Python

# 메모리: 34556KB / 시간: 88ms
from sys import stdin


input = stdin.readline

N = int(input())
building = [int(input()) for _ in range(N)]

stack = []
ret = 0
for b in building:
    while stack and stack[-1] <= b:
        stack.pop()
    stack.append(b)
    ret += len(stack) - 1

print(ret)

"""
[10]        ret += 0
[10, 3]     ret += 1
[10, 7]     ret += 1 (3은 7보다 작으므로 pop)
[10, 7, 4]  ret += 2
[12]        ret += 0 (10, 7, 4 모두 12보다 작으므로 pop)
[12, 2]     ret += 1

ret = 5
"""