# 문제집 - 0x11강 - 그리디


# 문제: https://www.acmicpc.net/problem/1439
# 메모리: 32412KB / 시간: 44ms
from sys import stdin


input = stdin.readline

S = input().rstrip()

cnt = [0, 0]
prev = 0

for s in S:
    if prev and prev != s:
        cnt[int(prev)] += 1
    prev = s

cnt[int(prev)] += 1

print(min(cnt))


# 다른 풀이 1. split()으로 간단하게 카운트...
s = input()
one = [x for x in s.split('0') if x != '']
zero = [x for x in s.split('1') if x != '']

print(min(len(one), len(zero)))


# 다른 풀이 2. 달라지는 횟수를 카운트를 이용.
s = input()
one = [x for x in s.split('0') if x != '']
zero = [x for x in s.split('1') if x != '']

print(min(len(one), len(zero)))