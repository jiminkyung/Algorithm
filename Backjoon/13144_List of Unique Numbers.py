# 문제집 - 0x14강 - 투 포인터


# 문제: https://www.acmicpc.net/problem/13144
# 메모리: 46492KB / 시간: 136ms
from sys import stdin


input = stdin.readline

N = int(input())
arr = list(map(int, input().split()))

nums = {}  # 수의 갯수를 체크할 딕셔너리

cnt = 0
left = 0

for right in range(N):
    nums[arr[right]] = nums.get(arr[right], 0) + 1

    # 현재 추가한 수의 갯수가 1이 될 때까지
    while nums[arr[right]] > 1:
        nums[arr[left]] -= 1  # 가장 왼쪽 인덱스의 숫자를 감소시킴
        left += 1
    
    cnt += right - left + 1  # 나올 수 있는 수열의 갯수 카운트

print(cnt)