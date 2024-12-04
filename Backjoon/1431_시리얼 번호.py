# 문제집 - 0x0F강 - 정렬 II


# 문제: https://www.acmicpc.net/workbook/view/7318
# 메모리: 31252KB / 시간: 36ms
from sys import stdin


input = stdin.readline

N = int(input())
serial = []

for _ in range(N):
    word = input().rstrip()
    num = 0
    for s in word:
        if s.isdigit():
            num += int(s)
    
    serial.append((len(word), num, word))

serial.sort()

for s in serial:
    print(s[2])