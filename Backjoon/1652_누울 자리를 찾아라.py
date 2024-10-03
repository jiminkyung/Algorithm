# 문제집 - 대학생 기본반


# 문제: https://www.acmicpc.net/problem/1652
# 메모리: 31120KB / 시간: 32ms
from sys import stdin


input = stdin.readline

N = int(input())

row = [list(input().rstrip()) for _ in range(N)]
col = zip(*row)

def counting(room):
    cnt = 0
    for line in room:
        tmp = 0
        for x in line:
            if x == ".":
                tmp += 1
            else:
                if tmp >= 2:
                    cnt += 1
                tmp = 0
        if tmp >= 2:
            cnt += 1
    return cnt

print(counting(row), counting(col))