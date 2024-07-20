# 그리디 알고리즘

# 메모리: 31120KB / 시간: 44ms
# 인출시간이 짧은 순서대로 정렬.
# curr = 현재까지 누적된 time값, total = curr값의 누적값(총 시간)

from sys import stdin


input = stdin.readline
N = int(input())
times = sorted(map(int, input().split()))

curr = total = 0

for time in times:
    curr += time
    total += curr

print(total)