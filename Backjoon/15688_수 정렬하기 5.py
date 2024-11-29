# 문제집 - 0x0E강 - 정렬 I


# 문제: https://www.acmicpc.net/problem/15688
# 메모리: 46876KB / 시간: 28096ms
from sys import stdin


input = stdin.readline

N = int(input())
nums = [0] * 2000001

for _ in range(N):
    n = int(input())
    nums[n] += 1

for i in range(-1000000, 1000001):
    if nums[i] > 0:
        for j in range(nums[i]):
            print(i)


# sort를 사용한 코드인데, 실행시간 2위다.
# 똑같이 사용해봤으나 시간초과... 이유는 모르겠음.
# https://www.acmicpc.net/source/84104715
import sys

input = sys.stdin.readline
N = int(input())
numbers = [int(input()) for _ in range(N)]
print('\n'.join(map(str, sorted(numbers))))