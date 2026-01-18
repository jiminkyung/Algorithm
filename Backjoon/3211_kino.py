# 그리디 알고리즘
# 정렬


# 문제: https://www.acmicpc.net/problem/3211
# 메모리: 33432KB / 시간: 1628ms
from sys import stdin


input = stdin.readline

def main():
    N = int(input())
    Z = [int(input()) for _ in range(N)]
    Z.sort()

    # k: 초대할 사람의 수
    for k in range(1, N+1):
        for i in range(k):
            # 미르코 + 자기자신을 제외하고 Z[i]명이 와야 함.
            # 즉, Z[i] < k 여야 가능.
            if Z[i] >= k:
                break
        else:
            print(k)
            break


main()