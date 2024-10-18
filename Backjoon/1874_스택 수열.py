# 문제집 - BOJ 길라잡이 베타 (1)


# 문제: https://www.acmicpc.net/problem/1874
# 메모리: 41252KB / 시간: 132ms
from sys import stdin


input = stdin.readline

N = int(input())
nums = [int(input()) for _ in range(N)]

stack, ret = [], []
is_True = True

i = 1
for num in nums:
    while i <= num:
        stack.append(i)
        ret.append("+")
        i += 1
    
    if stack[-1] == num:
        stack.pop()
        ret.append("-")
    else:
        is_True = False
        break

if is_True:
    print(*ret, sep="\n")
else:
    print("NO")