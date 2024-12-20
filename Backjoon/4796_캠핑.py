# 문제집 - 0x12강 - 수학


# 문제: https://www.acmicpc.net/problem/4796

"""
반례 link👉 https://www.acmicpc.net/board/view/110501
1 20 39
0 0 0
output = 20
answer = 2
"""
# 메모리: 32412KB / 시간: 32ms
from sys import stdin


input = stdin.readline

i = 1

while True:
    L, P, V = map(int, input().split())

    if (L, P, V) == (0, 0, 0):
        break
    
    day = (V//P) * L
    other = V % P

    if other > L:
        print(f"Case {i}: {day + L}")
    else:
        print(f"Case {i}: {day + other}")
    i += 1