# 문제집 - 대학생 기본반


# 문제: https://www.acmicpc.net/problem/1759
# 메모리: 31120KB / 시간: 32ms
from sys import stdin
from itertools import combinations


input = stdin.readline

L, C = map(int, input().split())
alphabet = sorted(input().rstrip().split())

for comb in combinations(alphabet, L):
    j = m = 0
    for c in comb:
        if c in "aeiou":
            m += 1
        else:
            j += 1
    
    if m < 1 or j < 2:
        continue
    print("".join(comb))