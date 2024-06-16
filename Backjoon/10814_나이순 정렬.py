# 정렬
# 메모리: 46140KB / 시간: 224ms

import sys


input = sys.stdin.readline
N = int(input())
members = []

for _ in range(N):
    age, name = input().split()
    members.append((int(age), name))

members.sort(key=lambda x: x[0])

for a, n in members:
    print(a, n)


# 실행시간 96ms인 코드.
# 1. 타입 힌트를 변수에도 적용할 수 있다.
# 2. readlines 함수

from sys import stdin

input = stdin.readlines


def solution() -> None:
    persons: list = input()[1:]
    persons.sort(key=lambda p: int(p.split()[0]))
    print(''.join(persons))


solution()