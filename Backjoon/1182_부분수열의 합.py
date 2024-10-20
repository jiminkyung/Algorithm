# 문제집 - BOJ 길라잡이 베타 (1)


# 문제: https://www.acmicpc.net/problem/1182
# 메모리: 31120KB / 시간: 320ms
from sys import stdin
from itertools import combinations


input = stdin.readline

N, S = map(int, input().split())
nums = list(map(int, input().split()))
ret = 0

for i in range(1, N+1):
    for comb in combinations(nums, i):
        if sum(comb) == S:
            ret += 1

print(ret)


# 실행시간 1위인 코드. 딕셔너리로 메모이제이션 사용.
# 출처👉 https://www.acmicpc.net/source/83478003
import sys
input = sys.stdin.readline

def memoization(subseq, d, prev, st):
    if prev in d: d[prev] += 1
    else: d[prev] = 1

    for i in range(st, len(subseq)):
        nxt = prev + subseq[i]
        memoization(subseq, d, nxt, i+1)

n, s = map(int, input().split())
seq = [*map(int, input().split())]

left, right = {}, {}
m = n//2

# 주어진 수열 seq을 반으로 나눠 메모이제이션 실행
memoization(seq[:m], left, 0, 0)
memoization(seq[m:], right, 0, 0)

# 만약 left를 l로 순회할때, s-l이 right에 존재한다면 left[l] * right[s-l]
cnt = sum(left[l] * right[s-l] for l in left.keys() if s-l in right)
print(cnt if s else cnt-1)