# 1차원 배열


# 문제: https://www.acmicpc.net/problem/2562
# 메모리: 31120KB / 시간: 32ms
from sys import stdin


input = stdin.readline

nums = [int(input()) for _ in range(9)]
ret = max(nums)

print(ret, nums.index(ret)+1, sep="\n")