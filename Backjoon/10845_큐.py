# 문제집 - BOJ 길라잡이 베타 (1)


# 문제: https://www.acmicpc.net/problem/10845
# 메모리: 34028KB / 시간: 60ms
from sys import stdin
from collections import deque


cmd = iter(stdin.read().split())
next(cmd)

queue = deque([])

for c in cmd:
    if c == "push":
        queue.append(next(cmd))
    elif c == "pop":
        print(queue.popleft() if queue else -1)
    elif c == "size":
        print(len(queue))
    elif c == "empty":
        print(int(not queue))
    elif c == "front":
        print(queue[0] if queue else -1)
    else:  # back
        print(queue[-1] if queue else -1)