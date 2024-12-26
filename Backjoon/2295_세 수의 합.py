# 문제집 - 0x13강 - 이분탐색


# 문제: https://www.acmicpc.net/problem/2295
# 메모리: 71040KB / 시간: 760ms
from sys import stdin


input = stdin.readline

N = int(input())
arr = sorted(int(input()) for _ in range(N))

two_sum = set()  # 두 수를 더한 값들을 미리 저장해둠.
for i in range(N):
    for j in range(i, N):
        two_sum.add(arr[i] + arr[j])

two_sum = sorted(two_sum)


def binary_search(target):
    start, end = 0, len(two_sum)-1

    while start <= end:
        mid = (start + end) // 2

        if two_sum[mid] == target:
            return True
        elif two_sum[mid] < target:
            start = mid + 1
        else:
            end = mid - 1
    return False


def finding():
    for k in range(N-1, -1, -1):
        d = arr[k]
        for i in range(N):
            c = d - arr[i]  # c = 두 수를 더한 값
            if c <= 0:
                continue
            # 만약 c가 two_sum 리스트에 존재한다면 조건을 만족하므로 바로 반환
            if binary_search(c):
                return d


print(finding())