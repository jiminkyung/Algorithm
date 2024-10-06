# 문제집 - 대학생 기본반


# 문제: https://www.acmicpc.net/problem/8979

# 첫 제출... 8점? => 공동등수 간과. 2등이 2명이어도 4등은 4등이어야 함.
# 메모리: 34016KB / 시간: 52ms
from sys import stdin
from collections import defaultdict


input = stdin.readline

N, K = map(int, input().split())
nation = defaultdict(list)

for _ in range(N):
    n, g, s, b = map(int, input().split())
    nation[g, s, b].append(n)

record = sorted(nation.keys(), reverse=True)
ret = 1
for rec in record:
    if K in nation[rec]:
        print(ret)
    ret += len(nation[rec])  # 공동등수 계산 부분 추가


# defaultdict 호출 없이 풀이한 코드. 실행시간, 메모리 모두 최소임.
# index 호출 시 동일값중 맨 앞에 위치한 값만 선택되기 때문에, 공동등수도 자연스럽게 계산됨. 젠장!
import sys

input = sys.stdin.readline

n, k = map(int, input().split())

nums, dic = [], dict()

for _ in range(n):
    p, *arr = map(int, input().split())
    nums.append(arr)
    dic[p] = arr

nums.sort(key=lambda x: (-x[0], -x[1], -x[2]))

print(nums.index(dic[k]) + 1)