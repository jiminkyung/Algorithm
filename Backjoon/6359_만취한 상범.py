# 문제집 - 0x12강 - 수학


# 문제: https://www.acmicpc.net/problem/6359
# 메모리: 32412KB / 시간: 32ms
from sys import stdin


input = stdin.readline

room = [True] * 101
room[0] = False

opened = [0] * 101
opened[1] = 1

for i in range(2, 101):
    for j in range(i, 101, i):
        if room[j]:
            room[j] = False
        else:
            room[j] = True
    opened[i] = sum(room[:i+1])

for _ in range(int(input())):
    n = int(input())
    print(opened[n])