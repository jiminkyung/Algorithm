# 문제집 - 0x13강 - 이분탐색


# 문제: https://www.acmicpc.net/problem/14921

# 2467_용액 문제와 거의 동일하다.
# 이 문제 역시 이분탐색보단 투 포인터를 사용하는쪽이 훨씬 빨랐다...

# 1. 투 포인터
# 메모리: 44748KB / 시간: 88ms
from sys import stdin


input = stdin.readline

N = int(input())
liquids = list(map(int, input().split()))

min_diff = liquids[0] + liquids[-1]
left, right = 0, N-1

while left < right:
    diff = liquids[left] + liquids[right]

    if abs(diff) < abs(min_diff):
        min_diff = diff
    
    if diff < 0:
        left += 1
    else:
        right -= 1


print(min_diff)


# 2. 이분탐색
# 메모리: 43724KB / 시간: 768ms
from sys import stdin


input = stdin.readline

N = int(input())
liquids = list(map(int, input().split()))

min_diff = float("inf")

for i in range(N-1):
    curr = liquids[i]

    start, end = i+1, N-1
    while start <= end:
        mid = (start + end) // 2
        diff = curr + liquids[mid]

        if abs(diff) < abs(min_diff):
            min_diff = diff
        
        if diff < 0:
            start = mid + 1
        else:
            end = mid - 1


print(min_diff)