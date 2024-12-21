# 문제집 - 0x12강 - 수학


# 문제: https://www.acmicpc.net/problem/10250
# 메모리: 32412KB / 시간: 44ms
from sys import stdin


input = stdin.readline

for _ in range(int(input())):
    H, W, N = map(int, input().split())
    floor = N % H
    if floor:
        print(floor * 100 + N//H + 1)
    else:
        print(H * 100 + N//H)