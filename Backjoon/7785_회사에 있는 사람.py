# 집합과 맵


# 첫번째 코드. 시간초과.
from sys import stdin


input = stdin.readline

n = int(input())
logs = []

for _ in range(n):
    name, state = input().split()
    if state == "leave":
        logs.remove(name)
    else:
        logs.append(name)

logs.sort(reverse=True)
print(*logs, sep="\n")


# 두번째 코드. 딕셔너리가 답이다!
# 메모리: 50284KB / 시간: 184ms
from sys import stdin


input = stdin.readline

n = int(input())
logs = {}

for _ in range(n):
    name, state = input().split()
    logs[name] = state
    if logs[name] == "leave":
        del logs[name]

ret = sorted(logs, reverse=True)
print(*ret, sep="\n")