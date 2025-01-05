# 문제집 - 0x14강 - 투 포인터


# 문제: https://www.acmicpc.net/problem/20922
# 메모리: 53288KB / 시간: 244ms
from sys import stdin


input = stdin.readline

N, K = map(int, input().split())
A = list(map(int, input().split()))

nums = {}

left = 0
ret = 0

for right in range(N):
    nums[A[right]] = nums.get(A[right], 0) + 1

    while nums[A[right]] > K:  # 현재 수가 K개 이하가 될 때까지 left 포인터 이동
        nums[A[left]] -= 1
        left += 1
    
    ret = max(right-left+1, ret)

print(ret)