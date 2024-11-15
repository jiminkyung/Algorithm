# 문제집 - 0x0C강 - 백트래킹


# 문제: https://www.acmicpc.net/problem/15665
# 중복 선택 O, 오름차순 출력

# 메모리: 31120KB / 시간: 632ms
from sys import stdin


input = stdin.readline

N, M = map(int, input().split())
nums = sorted(map(int, input().split()))

def backtrack(ret):
    if len(ret) == M:
        print(*ret)
        return
    
    curr = 0
    for i in range(N):
        if curr != nums[i]:
            ret.append(nums[i])
            curr = nums[i]
            backtrack(ret)
            ret.pop()

backtrack([])