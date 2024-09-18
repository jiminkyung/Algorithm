# 1차원 배열


# 문제: https://www.acmicpc.net/problem/10807
# 메모리: 31120KB / 시간: 36ms
from sys import stdin


input = stdin.readline

N = int(input())
cnt = [0] * 201

nums = list(map(int, input().split()))
for n in nums:
    cnt[n + 100] += 1

print(cnt[int(input()) + 100])