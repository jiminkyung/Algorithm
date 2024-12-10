# 그리디


# 문제: https://www.acmicpc.net/problem/32406
# 메모리: 61892KB / 시간: 160ms
from sys import stdin


input = stdin.readline

N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

ret = 0

# 마지막 두 열을 제외하고 볏단의 차이값을 더해줌
for i in range(N-2):
    ret += abs(A[i] - B[i])

a = A[N-1] + B[N-2]
b = B[N-1] + A[N-2]

ret += abs(a - b)
print(ret)