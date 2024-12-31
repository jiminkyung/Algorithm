# 문제집 - 0x13강 - 이분탐색


# 문제: https://www.acmicpc.net/problem/7453

# 2143_두 배열의 합 문제와 비슷하다. 하지만 이분탐색, 투 포인터 모두 사용할 수 없음... 시간초과다.

# PyPy3로 통과한 코드.
# Python3로 통과된 코드를 그대로 복붙해서 제출해봐도 시간초과가 뜸.

# 메모리: 1189744KB / 시간: 9732ms
from sys import stdin


input = stdin.readline

N = int(input())
A = []
B = []
C = []
D = []

for _ in range(N):
    a, b, c, d, = map(int, input().split())
    A.append(a)
    B.append(b)
    C.append(c)
    D.append(d)

sum_dic = {}

for i in range(N):
    for j in range(N):
        tmp = A[i] + B[j]
        sum_dic[tmp] = sum_dic.get(tmp, 0) + 1

cnt = 0

for i in range(N):
    for j in range(N):
        tmp = C[i] + D[j]
        cnt += sum_dic.get(-tmp, 0)

print(cnt)