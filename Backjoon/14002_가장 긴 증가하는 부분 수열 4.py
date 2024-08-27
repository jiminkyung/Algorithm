# 동적 계획법과 최단거리 역추적


# 메모리: 31120KB / 시간: 116ms

from sys import stdin


input = stdin.readline
N = int(input())
A = list(map(int, input().split()))

dp = [1] * N  # 길이를 저장할 리스트
path = [-1] * N  # 지나온 값을 저장할 리스트  # 👇역추적을 인덱스값이 0이 될때까지 반복하므로, -1로 초기화해준다.

for i in range(1, N):
    for j in range(i):
        if A[i] > A[j] and dp[i] < dp[j] + 1:
            dp[i] = dp[j] + 1
            path[i] = j  # dp[i]가 재할당될때 path[i]값을 j로 저장한다.

length = max(dp)  # LIS의 길이
idx = dp.index(length)  # LIS의 마지막 원소의 인덱스

LIS = []
while idx >= 0:  # 인덱스가 0이 될때까지 반복
    LIS.append(A[idx])  # A[idx] 값을 리스트에 저장한후, path의 idx번째 원소값(인덱스값)을 idx로 재할당한다.
    idx = path[idx]

LIS.reverse()  # 순서대로 출력해야 하므로 뒤집는다!

print(length)
print(*LIS)