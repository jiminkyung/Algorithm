# 문제집 - 0x07강 - 덱


# 문제: https://www.acmicpc.net/problem/11003

# 일단 짜본 코드. 이걸 덱을 사용해서 구현하려면?
from sys import stdin


input = stdin.readline

N, L = map(int, input().split())
nums = list(map(int, input().split()))
D = []

for i in range(N):
    tmp = int(1e9)
    for j in range(i-L+1, i+1):
        if j < 0:
            continue
        tmp = min(tmp, nums[j])
    D.append(tmp)

print(*D)


# 메모리: 644816KB / 시간: 6380ms
from sys import stdin
from collections import deque


input = stdin.readline

N, L = map(int, input().split())
nums = list(map(int, input().split()))
D = []
dq = deque([])  # 최소값의 인덱스를 저장할 리스트

for i in range(N):
    # 만약 dq의 최솟값 인덱스가 범위를 벗어났다면 popleft()
    if dq and dq[0] < i - L + 1:
        dq.popleft()

    # dq의 마지막 최솟값 인덱스에 해당하는 nums값이 현재 nums값보다 크다면,
    # dq[-1]역시 범위 내에 속하지만, 이보다 nums값이 더 작다는 뜻이므로 pop()
    while dq and nums[dq[-1]] > nums[i]:
        dq.pop()
    
    dq.append(i)
    # 결과 리스트에 범위 내의 최솟값을 추가
    D.append(nums[dq[0]])

print(*D)