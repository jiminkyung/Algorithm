# 동적 계획법 3


# 문제: https://www.acmicpc.net/problem/11723
# 다 풀고 찾아보니 단순히 append, remove로 조작하는게 더 빠른듯하다.

# 메모리: 31120KB / 시간: 3592ms
from sys import stdin


input = stdin.readline

M = int(input())
S = [0] * 21

for _ in range(M):
    cmd, *x = input().rstrip().split()
    
    if cmd == "add":
        if S[int(x[0])] == 0:
            S[int(x[0])] = 1
    elif cmd == "remove":
        if S[int(x[0])] != 0:
            S[int(x[0])] = 0
    elif cmd == "check":
        print(int(S[int(x[0])] != 0))
    elif cmd == "toggle":
        if S[int(x[0])] == 0:
            S[int(x[0])] = 1
        else:
            S[int(x[0])] = 0
    elif cmd == "all":
        S = [1] * 21
    else:
        S = [0] * 21