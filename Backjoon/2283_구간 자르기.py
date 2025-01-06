# 문제집 - 0x14강 - 투 포인터


# 문제: https://www.acmicpc.net/problem/2283

# ⭐ 스위핑, 누적합, 투포인터를 모두 사용해야 시간초과 없이 풀 수 있는 문제다.
# 메모리: 71968KB / 시간: 744ms
from sys import stdin


input = stdin.readline

N, K = map(int, input().split())

ret = (0, 0)
vertical = [0] * 1000001
max_len = 0

for _ in range(N):
    x, y = map(int, input().split())
    # 구간이 x부터 시작함을 나타냄.
    # vertical[n]: n~n+1에 포함되는 구간의 갯수
    vertical[x] += 1
    vertical[y] -= 1
    max_len = max(y, max_len)

for i in range(1, 1000001):
    vertical[i] += vertical[i-1]


left = right = 0
S = 0

while left <= right and right <= max_len:
    if S == K:
        ret = (left, right)
        break

    if S < K:
        S += vertical[right]
        right += 1
    else:
        S -= vertical[left]
        left += 1

print(*ret)