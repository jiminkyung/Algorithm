# 문제집 - 0x0C강 - 백트래킹


# 문제: https://www.acmicpc.net/problem/15663
# 같은 숫자가 여러개 주어짐. [1, 2, 3, 3]일때, 3번째의 3과 4번째의 3은 다른 3이다.
# 중복 선택 X, 오름차순 출력

# 메모리: 31120KB / 시간: 68ms
from sys import stdin


input = stdin.readline

N, M = map(int, input().split())
nums = sorted(map(int, input().split()))
used = [False] * N

ret = []

def backtrack(ret):
    if len(ret) == M:
        print(" ".join(map(str, ret)))
        return
    
    curr = 0
    for i in range(N):
        # i번째 숫자를 사용하지 않았고 이전 숫자와 다른값이라면
        if not used[i] and curr != nums[i]:
            used[i] = True
            ret.append(nums[i])
            curr = nums[i]
            backtrack(ret)
            ret.pop()
            used[i] = False

backtrack([])