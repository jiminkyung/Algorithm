# 1차원 배열


# 문제: https://www.acmicpc.net/problem/10871
# 메모리: 32140KB / 시간: 36ms
from sys import stdin


input = stdin.readline

N, K = map(int, input().split())
A = list(map(int, input().split()))

ret = [num for num in A if num < K]
print(*ret)