# 그리디 알고리즘

# 메모리: 51900KB / 시간: 240ms
# 회의가 빨리 끝나는 순으로, 끝나는 시간이 같다면 더 빨리 시작하는 순서대로 정렬.

from sys import stdin


input = stdin.readline
N = int(input())

times = []
for _ in range(N):
    times.append(tuple(map(int, input().split())))

times.sort(key=lambda x: (x[1], x[0]))

ret = point = 0

for start, end in times:
    if point <= start:
        ret += 1
        point = end

print(ret)