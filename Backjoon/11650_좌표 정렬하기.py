# 정렬
# 메모리: 51900KB / 시간: 336ms

# 풀고나서 찾아보니 오름차순, 기준이 x -> y 이므로 별다른 key값없이 그냥 sort()만 해줘도 됐었다.

import sys


input = sys.stdin.readline

N = int(input())
points = []

for _ in range(N):
    x, y = map(int, input().split())
    points.append((x, y))

points.sort(key=lambda x: (x[0], x[1]))

for x, y in points:
    print(x, y)