# 문제집 - 0x03강 - 배열


# 문제: https://www.acmicpc.net/problem/13300
# 메모리: 32412KB / 시간: 40ms
from sys import stdin


input = stdin.readline

N, K = map(int, input().split())
student = [[0, 0] for _ in range(6)]

for _ in range(N):
    gen, grade = map(int, input().split())
    student[grade-1][gen] += 1

room = 0

for s in student:
    room += (s[0] - 1) // K + 1
    room += (s[1] - 1) // K + 1

print(room)