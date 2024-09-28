# 문자열


# 문제: https://www.acmicpc.net/problem/2675
# 메모리: 31120KB / 시간: 28ms
from sys import stdin


input = stdin.readline

T = int(input())
for _ in range(T):
    R, S = input().rstrip().split()
    R = int(R)

    ret = []
    for s in S:
        ret.append(s * R)
    print(*ret, sep="")