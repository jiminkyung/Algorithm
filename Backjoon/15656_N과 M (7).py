# 문제집 - 0x0C강 - 백트래킹


# 문제: https://www.acmicpc.net/problem/15656
# 메모리: 31120KB / 시간: 1348ms
from sys import stdin


input = stdin.readline

N, M = map(int, input().split())
nums = sorted(map(int, input().split()))

def backtrack(ret):
    if len(ret) == M:
        print(" ".join(map(str, ret)))
        return
    
    for i in range(N):
        ret.append(nums[i])
        backtrack(ret)
        ret.pop()

backtrack([])