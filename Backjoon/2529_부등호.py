# 문제집 - 대학생 기본반


# 문제: https://www.acmicpc.net/problem/2529

# 1) permutations, 2) 백트래킹, 3) DFS
# 백트래킹을 사용한 풀이가 가장 효율적임.
# 1987_알파벳 문제같은 경우, set()을 이용한 DFS가 가장 빨랐으나...
# 문제 유형에 따라 어떤 자료형/메서드를 사용할지 고민해봐야겠다.

# 1. permutations를 사용한 풀이.
# 메모리: 32140KB / 시간: 1496ms
from sys import stdin
from itertools import permutations


input = stdin.readline

k = int(input())
signs = list(input().rstrip().split())
ret = []

def check(perm):
    for i in range(k):
        if signs[i] == "<":
            if perm[i] >= perm[i+1]:  # 부등호과 맞지 않다면 바로 False 리턴.
                return False
        else:
            if perm[i] <= perm[i+1]:
                return False
    return True

for perm in permutations("0123456789", k + 1):
    if check(perm):
        ret.append("".join(perm))

print(ret[-1], ret[0], sep="\n")


# 2. 백트래킹을 사용한 풀이
# 메모리: 32140KB / 시간: 124ms
from sys import stdin


input = stdin.readline

def check(a, b, op):
    if op == "<":
        return a < b
    else:
        return a > b

def dfs(idx: int, nums: str, used: list):
    if idx == k + 1:
        ret.append(nums)
        return
    
    for i in range(10):
        if not used[i]:
            # 첫번째 인덱스값은 무조건 추가해줘야하므로 idx == 0 조건 추가.
            if idx == 0 or check(int(nums[-1]), i, signs[idx-1]):
                used[i] = True
                dfs(idx + 1, nums + str(i), used)
                used[i] = False

k = int(input())
signs = list(input().rstrip().split())

ret = []
used = [False] * 10  # 0~9 사용여부를 저장하는 리스트

dfs(0, "", used)
print(ret[-1], ret[0], sep="\n")


# 3. 일반적인 DFS를 사용한 풀이
# 메모리: 32140KB / 시간: 172ms
from sys import stdin


input = stdin.readline

def check(a, b, op):
    return a < b if op == "<" else a > b

def dfs():
    stack = [(0, "")]

    while stack:
        idx, nums= stack.pop()

        if idx == k + 1:
            ret.append(nums)
            continue

        for i in range(10):
            if str(i) not in nums:
                if idx == 0 or check(int(nums[-1]), i, signs[idx-1]):
                    stack.append((idx + 1, nums + str(i)))
    return ret[0], ret[-1]  # 스택 특성상 최소값이 가장 마지막에 체크되므로 ret에 가장 마지막 원소는 최소값이 됨.


k = int(input())
signs = list(input().rstrip().split())
ret = []

max_ret, min_ret = dfs()
print(max_ret, min_ret, sep="\n")