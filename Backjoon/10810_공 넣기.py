# 1차원 배열


# 문제: https://www.acmicpc.net/problem/10810
# 문제가 왜 익숙한지 모르겠다... 분명 어디서 본 문제같은데...

# 메모리: 31252KB / 시간: 36ms
from sys import stdin


input = stdin.readline

N, M = map(int, input().split())
balls = [0] * (N+1)

for _ in range(M):
    i, j, k = map(int, input().split())  # i부터 j까지 k 할당
    for number in range(i, j+1):
        balls[number] = k

print(*balls[1:])