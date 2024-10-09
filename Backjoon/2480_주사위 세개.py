# 조건문


# 문제: https://www.acmicpc.net/problem/2480
# 메모리: 31120KB / 시간: 32ms
dice = [0] * 7
ret = 0

for d in map(int, input().split()):
    dice[d] += 1

if 3 in dice:
    ret = 10000 + dice.index(3) * 1000
elif 2 in dice:
    ret = 1000 + dice.index(2) * 100
else:
    ret = (6 - dice[::-1].index(1)) * 100

print(ret)