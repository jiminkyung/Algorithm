# 문제집 - BOJ 길라잡이 베타 (1)


# 문제: https://www.acmicpc.net/problem/6603
# 메모리: 31120KB / 시간: 36ms
from sys import stdin


# 조합 함수 구현
def combination(arr, n):
    ret = []

    if n == 0:
        return [[]]

    for i in range(len(arr) - n + 1):
        for comb in combination(arr[i+1:], n-1):
            ret.append([arr[i]] + comb)
    return ret

for line in stdin:
    if line == "0\n":
        break

    k, *nums = list(map(int, line.split()))
    arr = combination(nums, 6)
    for a in arr:
        print(*a)
    print()