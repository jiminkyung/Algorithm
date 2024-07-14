# 동적 계획법 1

# 바이토닉 수열 = LIS(증가부분수열) + LDS(감소부분수열) - 1
# AI선생님의 도움을 받은 풀이...
# 메모리: 31252KB / 시간: 100ms

from sys import stdin


input = stdin.readline
N = int(input())
A = list(map(int, input().split()))

def bitonic():
    lis = [1] * N
    lds = [1] * N

    for i in range(1, N):  # LIS
        for j in range(i):
            if A[i] > A[j] and lis[i] < lis[j] + 1:
                lis[i] = lis[j] + 1
    
    for i in range(N-2, -1, -1):  # LDS
        for j in range(N-1, i, -1):
            if A[i] > A[j] and lds[i] < lds[j] + 1:
                lds[i] = lds[j] + 1
    
    max_length = 0
    for i in range(N):
        max_length = max(max_length, lis[i] + lds[i] - 1)
    
    return max_length

print(bitonic())