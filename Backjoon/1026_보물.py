# 문제집 - 대학생 기본반


# 문제: https://www.acmicpc.net/problem/1026
# 문제에서 'B는 재배열하면 안된다'고 했는데, 신경쓰지않고 풀었다.

# 메모리: 31120KB / 시간: 36ms
from sys import stdin


input = stdin.readline

N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

A.sort()
B.sort(reverse=True)

ret = 0
for i in range(N):
    ret += A[i] * B[i]

print(ret)


# B를 그대로 두고 풀어보기. => 왜 이게 더 빠르지...?
# 메모리: 31120KB / 시간: 36ms
from sys import stdin


input = stdin.readline

N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

idx = list(range(N))
idx.sort(key=lambda x: -B[x])

A.sort()
B_sorted = [B[i] for i in idx]

s = sum(a * b for a, b in zip(A, B_sorted))
print(s)