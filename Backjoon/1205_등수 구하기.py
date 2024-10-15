# 문제집 - 대학생 기본반


# 문제: https://www.acmicpc.net/problem/1205
from sys import stdin


input = stdin.readline

N, new, P = map(int, input().split())

if N == 0:
    print(1)
else:
    score = list(map(int, input().split()))
    score.sort(reverse=True)
    
    if N < P or score[P-1] < new:
        score.append(new)
        score.sort(reverse=True)
        print(score.index(new) + 1)
    else:
        print(-1)