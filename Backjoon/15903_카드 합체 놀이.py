# 문제집 - 0x11강 - 그리디


# 문제: https://www.acmicpc.net/problem/15903
# 메모리: 32412KB / 시간: 212ms
from sys import stdin


input = stdin.readline

n, m = map(int, input().split())
a = sorted(map(int, input().split()))

# m번동안 가장 작은 두 수를 더한 값으로 업데이트한 뒤 정렬한다.
for _ in range(m):
    a[0] = a[1] = a[0] + a[1]
    a.sort()

print(sum(a))