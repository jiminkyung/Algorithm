# 문제집 - 0x03강 - 배열


# 문제: https://www.acmicpc.net/problem/1475
# 메모리: 31120KB / 시간: 40ms
from sys import stdin


plastic = stdin.readline().rstrip().replace("6", "9")
number = [0] * 10

for p in plastic:
    number[int(p)] += 1

number[9] = number[9] // 2 + number[9] % 2
print(max(number))