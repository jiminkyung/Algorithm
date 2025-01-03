# 문제집 - 0x14강 - 투 포인터


# 문제: https://www.acmicpc.net/problem/22862

# 처음엔 odd_idx 리스트를 통해 홀수의 인덱스를 저장, pop(0)하여 left를 조정하는 방식을 사용했으나 시간초과.
# while문으로 start번째 수를 체크하며 홀수 카운트를 조정하는 방식으로 변경.
# 메모리: 132864KB / 시간: 828ms
from sys import stdin


input = stdin.readline

N, K = map(int, input().split())
arr = list(map(int, input().split()))

max_len = odd_cnt = 0
left = 0

for right in range(N):
    if arr[right] % 2 != 0:
        odd_cnt += 1
    
    while odd_cnt > K:
        if arr[left] % 2 != 0:
            odd_cnt -= 1
        left += 1
    
    max_len = max(right-left+1 - odd_cnt, max_len)

print(max_len)