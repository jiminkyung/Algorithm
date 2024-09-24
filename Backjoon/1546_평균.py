# 1차원 배열


# 문제: https://www.acmicpc.net/problem/1546
# 메모리: 31120KB / 시간: 32ms
from sys import stdin


input = stdin.readline

N = int(input())
score = list(map(int, input().split()))

t = max(score)
for i in range(N):
    score[i] = score[i] / t * 100

print(sum(score) / N)