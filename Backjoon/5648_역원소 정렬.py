# 문제집 - 0x0F강 - 정렬 II


# 문제: https://www.acmicpc.net/problem/5648
# 메모리: 32140KB / 시간: 44ms
from sys import stdin


nums = [*stdin.read().split()[1:]]
ret = []
for num in nums:
    ret.append(int(num[::-1]))

ret.sort()
print(*ret, sep="\n")