# 문제집 - 0x0F강 - 정렬 II


# 문제: https://www.acmicpc.net/problem/2910
# 메모리: 31120KB / 시간: 32ms
from sys import stdin


input = stdin.readline

N, C = map(int, input().split())
nums = {}

for num in map(int, input().split()):
    nums[num] = nums.get(num, 0) + 1

ret = [*nums.items()]
ret.sort(key=lambda x: -x[1])  # 빈도가 같다면 작성된 순서대로

for num, cnt in ret:
    for _ in range(cnt):
        print(num, end=" ")