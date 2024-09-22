# 1차원 배열


# 문제: https://www.acmicpc.net/problem/5597
# 메모리: 31120KB / 시간: 32ms
from sys import stdin


input = stdin.readline

number = [False] * 31

for _ in range(28):
    number[int(input())] = True

for i in range(1, 31):
    if not number[i]:
        print(i)