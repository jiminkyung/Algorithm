# 문제집 - BOJ 길라잡이 베타 (1)


# 문제: https://www.acmicpc.net/problem/2217
# [2, 10, 15]일때를 가정해보자. 15를 선택하면 최대 15, 10을 추가로 선택하면 한 로프로 감당할 수 있는 무게는 최대 10이다.
# 즉, 총 무게를 10 * 2 = 20이 된다.

# 메모리: 35364KB / 시간: 116ms
from sys import stdin


input = stdin.readline

N = int(input())
rope = sorted(int(input()) for _ in range(N))
ret = 0

for r in rope:
    ret = max(ret, r * N)
    N -= 1

print(ret)