# 1차원 배열


# 문제: https://www.acmicpc.net/problem/10818
# 메모리: 116712KB / 시간: 340ms
from sys import stdin


input = stdin.readline

N = int(input())
min, max = float("inf"), float("-inf")

for n in map(int, input().split()):
    if n < min:
        min = n
    if n > max:
        max = n

print(min, max)


# max, min 함수를 쓰는게 더 빠르다.
# 메모리: 152796KB / 시간: 332ms
from sys import stdin


input = stdin.readline

N = int(input())
nums = list(map(int, input().split()))

print(min(nums), max(nums))