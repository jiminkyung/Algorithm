# 이분 탐색

# 메모리: 47408KB / 시간: 444ms

from sys import stdin


input = stdin.readline

N = int(input())
A = sorted(map(int, input().split()))

M = int(input())
nums = list(map(int, input().split()))

def binary_search(target, start, end) -> int:
    if start > end:
        return 0
    
    mid = (start + end) // 2

    if A[mid] == target:
        return 1
    elif A[mid] < target:
        return binary_search(target, mid+1, end)
    else:
        return binary_search(target, start, mid-1)

for num in nums:
    print(binary_search(num, 0, N-1))