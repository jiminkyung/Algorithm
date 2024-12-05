# 문제집 - 0x0F강 - 정렬 II


# 문제: https://www.acmicpc.net/problem/11656
# 메모리: 31120KB / 시간: 36ms
from sys import stdin


S = stdin.readline().rstrip()
strings = []

for i in range(len(S)):
    strings.append(S[i:])

strings.sort()
print(*strings, sep="\n")