# 문제집 - 대학생 기본반


# 문제: https://www.acmicpc.net/problem/2661
# 메모리: 31120KB / 시간: 36ms
from sys import stdin


N = int(stdin.readline())

def check(num):
    for i in range(1, len(num)//2 + 1):
        if num[-i:] == num[-(i*2):-i]:
            return False
    return True

def backtrack(num, l):
    if l == N:
        print(num)
        exit(0)
    for n in "123":
        if check(num + str(n)):
            backtrack(num + str(n), l + 1)

backtrack("", 0)