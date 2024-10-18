# 문제집 - BOJ 길라잡이 베타 (1)


# 문제: https://www.acmicpc.net/problem/10867
# 메모리: 38476KB / 시간: 56ms

# 🚨str형태 그대로 정렬시, [-5, -3, -1]이 아닌 [-1, -3, -5]형태로 정렬됨. 음수값이 제대로 정렬되지 않음.
from sys import stdin


input = stdin.readline

N = int(input())
nums = set(map(int, input().split()))
nums = sorted(nums)

print(*nums)