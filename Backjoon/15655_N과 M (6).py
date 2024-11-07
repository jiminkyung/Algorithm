# 문제집 - 0x0C강 - 백트래킹


# 문제: https://www.acmicpc.net/problem/15655
# 메모리: 31120KB / 시간: 32ms
from sys import stdin


input = stdin.readline

N, M = map(int, input().split())
nums = sorted(map(int, input().split()))

def backtrack(start, ret):
    if len(ret) == M:
        print(" ".join(map(str, ret)))
        return
    
    for i in range(start, N):
        ret.append(nums[i])
        backtrack(i+1, ret)
        ret.pop()

backtrack(0, [])