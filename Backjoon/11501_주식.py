# 문제집 - 0x11강 - 그리디


# 문제: https://www.acmicpc.net/problem/11501
# 메모리: 164888KB / 시간: 3780ms
from sys import stdin


input = stdin.readline

T = int(input())
for _ in range(T):
    N = int(input())
    stocks = list(map(int, input().split()))

    stack = []
    surplus = 0  # 흑자

    # 처음엔 순방향으로 체크했으나 틀림.
    # 반례👉 https://www.acmicpc.net/board/view/130261
    # 현재까지의 제일 큰 값보다 더 큰 값이 나올때까지 모아놔야함.
    for i in range(N-1, -1, -1):
        if stack and stack[0] < stocks[i]:
            top = stack.pop(0)
            for s in stack:
                surplus += top - s
            stack = []
        stack.append(stocks[i])

    if stack:
        top = stack.pop(0)
        for s in stack:
            surplus += top - s
    
    print(surplus)