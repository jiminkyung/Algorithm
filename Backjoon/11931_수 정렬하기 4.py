# 문제집 - 0x0E강 - 정렬 I


# 문제: https://www.acmicpc.net/problem/11931
# sort()와 reverse를 사용해도 통과할 수 있지만, 메모리와 시간 모두 아래 방식이 효율적이다.

# 메모리: 46744KB / 시간: 1108ms
from sys import stdin


input = stdin.readline

N = int(input())
nums = [False] * 2000001

for _ in range(N):
    n = int(input())
    nums[n] = True

# 내림차순으로 출력해야하므로 거꾸로 순회
for i in range(1000000, -1000001, -1):
    if nums[i]:
        print(i)