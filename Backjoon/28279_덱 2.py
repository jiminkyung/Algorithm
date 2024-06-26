# 스택, 큐, 덱
# 메모리: 131408KB / 시간: 408ms

from collections import deque
import sys


cmd = iter(sys.stdin.read().split())
next(cmd)

dq = deque()
ret = []

for c in cmd:
    if c == "1":
        dq.appendleft(next(cmd))
    elif c == "2":
        dq.append(next(cmd))
    elif c == "3":
        ret.append(dq.popleft() if dq else "-1")
    elif c == "4":
        ret.append(dq.pop() if dq else "-1")
    elif c == "5":
        ret.append(str(len(dq)))
    elif c == "6":
        ret.append("1" if not dq else "0")
    elif c == "7":
        ret.append(dq[0] if dq else "-1")
    else:
        ret.append(dq[-1] if dq else "-1")

sys.stdout.write("\n".join(ret))


# 실행시간을 줄여보자.
# 메모리: 102344KB / 시간: 864ms
# 메모리용량은 줄어들었으나 시간이 두배가량 증가...
from collections import deque
from sys import stdin


input = stdin.readline

N = int(input())
dq = deque()

commands = {
    "1": dq.appendleft,
    "2": dq.append,
    "3": lambda: print(dq.popleft() if dq else -1),
    "4": lambda: print(dq.pop() if dq else -1),
    "5": lambda: print(len(dq)),
    "6": lambda: print(int(not dq)),
    "7": lambda: print(dq[0] if dq else -1),
    "8": lambda: print(dq[-1] if dq else -1)
}

for _ in range(N):
    cmd, *num = input().split()
    if cmd in "12":
        commands[cmd](num[0])
    else:
        commands[cmd]()