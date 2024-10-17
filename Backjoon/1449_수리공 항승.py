# 문제집 - 대학생 기본반


# 문제: https://www.acmicpc.net/problem/1449
# 메모리: 31120KB / 시간: 36ms
from sys import stdin


input = stdin.readline

N, L = map(int, input().split())
place = list(map(int, input().split()))
place.sort()

tape, length = 1, 0

for i in range(N-1):
    length += place[i+1] - place[i]
    
    if length+1 > L:  # 양 옆으로 0.5의 여유를 둬야함.
        tape += 1
        length = 0

print(tape)