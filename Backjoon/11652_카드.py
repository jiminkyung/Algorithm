# 문제집 - 0x0F강 - 정렬 II


# 문제: https://www.acmicpc.net/problem/11652
# 메모리: 50084KB / 시간: 124ms
from sys import stdin


input = stdin.readline

N = int(input())
number = {}

for _ in range(N):
    n = int(input())
    number[n] = number.get(n, 0) + 1

# (키, 값)으로 언패킹
number = [*number.items()]
number.sort(key=lambda x: (-x[1], x[0]))

print(number[0][0])