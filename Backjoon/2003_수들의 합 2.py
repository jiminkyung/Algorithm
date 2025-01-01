# 문제집 - 0x14강 - 투 포인터


# 문제: https://www.acmicpc.net/problem/2003

# 양 끝에서 좁혀가는 방식이 아닌 범위를 넓혀가는 방식으로 풀어야한다.
# 메모리: 33432KB / 시간: 36ms
from sys import stdin


input = stdin.readline

N, M = map(int, input().split())
A = list(map(int, input().split()))

left = right = 0
curr_sum = 0
cnt = 0

while left <= right and right < N:
    curr_sum += A[right]
    right += 1

    while curr_sum > M:
        curr_sum -= A[left]
        left += 1
    
    if curr_sum == M:
        cnt += 1


print(cnt)


# 아래 방식이 더 깔끔하다.
# for문으로 N번째 원소까지 end를 증가시킴.
# 메모리: 33432KB / 시간: 40ms
from sys import stdin


input = stdin.readline

N, M = map(int, input().split())
A = list(map(int, input().split()))

start = 0
curr_sum = 0
cnt = 0

for end in range(N):
    curr_sum += A[end]
    
    # curr_sum이 M보다 크면 start를 증가시켜 합을 줄임
    while curr_sum > M and start <= end:
        curr_sum -= A[start]
        start += 1
    
    if curr_sum == M:
        cnt += 1

print(cnt)