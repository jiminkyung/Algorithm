# 정렬
# 메모리: 51900KB / 시간: 340ms
# 11650(좌표 정렬하기) 문제와 기준만 다름.

import sys


input = sys.stdin.readline

N = int(input())
points = []

for _ in range(N):
    x, y = map(int, input().split())
    points.append((x, y))

points.sort(key=lambda x: (x[1], x[0]))

for x, y in points:
    print(x, y)