# 문제집 - 0x11강 - 그리디


# 문제: https://www.acmicpc.net/problem/2847
# 메모리: 32412KB / 시간: 108ms
from sys import stdin


input = stdin.readline

N = int(input())

scores = [int(input()) for _ in range(N)]
cnt = 0

# 마지막 레벨을 기준으로 진행. 현재 레벨을 기준으로 전단계 레벨을 조정.
for i in range(N-1, 0, -1):
    while scores[i] <= scores[i-1]:
        scores[i-1] -= 1
        cnt += 1

print(cnt)