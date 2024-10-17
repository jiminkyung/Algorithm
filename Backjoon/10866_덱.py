# 문제집 - BOJ 길라잡이 베타 (1)


# 문제: https://www.acmicpc.net/problem/10866
# 메모리: 34036KB / 시간: 64ms
from sys import stdin
from collections import deque


cmd = iter(stdin.read().split())
next(cmd)

deq = deque([])

for c in cmd:
    if c == "push_front":
        deq.appendleft(next(cmd))
    elif c == "push_back":
        deq.append(next(cmd))
    elif c == "pop_front":
        print(deq.popleft() if deq else -1)
    elif c == "pop_back":
        print(deq.pop() if deq else -1)
    elif c == "size":
        print(len(deq))
    elif c == "empty":
        print(int(not deq))
    elif c == "front":
        print(deq[0] if deq else -1)
    else:  # back
        print(deq[-1] if deq else -1)