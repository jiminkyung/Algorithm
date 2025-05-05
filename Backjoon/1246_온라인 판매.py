# 정렬
# 그리디 알고리즘


# 문제: https://www.acmicpc.net/problem/1246
# 메모리: 32412KB / 시간: 32ms
from sys import stdin


input = stdin.readline

def main():
    N, M = map(int, input().split())
    eggs = [int(input()) for _ in range(M)]
    # max_money: 총 최대 수익, max_cost: 최대 달걀 가격
    max_money = max_cost = 0

    eggs.sort()

    # (M-i)명의 고객이 살 수 있을때의 최대 수익 == eggs[i]
    # 달걀의 총 갯수 N이 (M-i)보다 적다면, N개만큼만 팔 수 있음.
    for i in range(M):
        money = (M-i) * eggs[i] if (M-i) <= N else N * eggs[i]
        if money > max_money:
            max_money = money
            max_cost = eggs[i]
    
    print(max_cost, max_money)


main()