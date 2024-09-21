# 1차원 배열


# 문제: https://www.acmicpc.net/problem/10813
# 메모리: 31120KB / 시간: 32ms
from sys import stdin


input = stdin.readline

N, M = map(int, input().split())
balls = list(range(N+1))

for _ in range(M):
    i, j = map(int, input().split())
    balls[i], balls[j] = balls[j], balls[i]

print(*balls[1:])