# 심화 2
# 메모리: 43596KB / 시간: 72ms

from sys import stdin


logs = iter(stdin.read().split())
next(logs)
ret = 0
curr = set()

for log in logs:
    if log == "ENTER":
        curr = set()
        continue

    if log in curr:
        continue
    else:
        curr.add(log)
        ret += 1

print(ret)


# 더 간단한 방법.
# 메모리: 44548KB / 시간: 60ms
from sys import stdin


logs = iter(stdin.read().split("ENTER"))

ret = sum(len(set(log.split())) for log in logs) - 1
print(ret)