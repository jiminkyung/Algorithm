# 문자열


# 문제: https://www.acmicpc.net/problem/9086
# 메모리: 31120KB / 시간: 32ms
from sys import stdin


input = stdin.readline

T = int(input())
for _ in range(T):
    word = input().rstrip()
    print(word[0], word[-1], sep="")