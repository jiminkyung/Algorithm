# 1차원 배열


# 문제: https://www.acmicpc.net/problem/3052

# 배열 대신 set으로 풀이.
# 메모리: 31120KB / 시간: 28ms
from sys import stdin


input = stdin.readline

ret = set()
for _ in range(10):
    ret.add(int(input()) % 42)

print(len(ret))


# 문제의 의도에 맞게 1차원 배열로 풀어보자~
# 메모리: 31120KB / 시간: 32ms
from sys import stdin


input = stdin.readline

namerge = [False] * 42

for _ in range(10):
    namerge[int(input()) % 42] = True

print(sum(namerge))